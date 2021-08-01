#Limit##
from manim import*
import numpy as np
class Definition_by_graph(Scene):
	def get_horizontall_lines_to_graph(
		self, graph, x_min=None, x_max=None, num_lines=20, **kwargs
	):
		y_min = y_min or self.y_min
		y_max = y_max or self.y_max
		return VGroup(
			*[
				self.get_vertical_line_to_graph(y, graph, **kwargs)
				for y in np.linspace(y_min, y_max, num_lines)
			]
		)

	def construct(self):
		ax = Axes(
			x_range = [-1,10,1], 
			y_range = [-1,7,1],
		)
		labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

		curve = ax.get_graph(lambda x: 0.12*x**2+0.5, x_range = [1,7], color = BLUE)
		
		#a_label
		adot = Dot(color = BLACK, radius = 0.001, stroke_width=0)
		adot.move_to(ax.coords_to_point(5, 0), UP)
		a_tex = Tex("a").next_to(adot,DOWN).scale(0.5)

		#L_label
		ldot = Dot(color = BLACK, radius = 0.001, stroke_width=0)
		ldot.move_to(ax.coords_to_point(0, 3), RIGHT)
		l_tex = MathTex(r'L').next_to(ldot,LEFT).scale(0.5)

		self.add(ax,a_tex,adot,ldot,l_tex)
		self.get_delta()
		self.play(Write(curve))
		

		#Delta L
	def get_delta(self):
		ax = Axes(
			x_range = [-1,10,1], 
			y_range = [-1,7,1],
		)
		
		l = 3
		delta_l = 0.5
		
		dlpdot = Dot(color = BLACK, radius = 0.001, stroke_width=0)
		dlpdot.move_to(ax.coords_to_point(0, l+delta_l), RIGHT)
		dlp_tex = MathTex(r'L+\varepsilon').next_to(dlpdot,LEFT).scale(0.5)
		dlp_line = DashedVMobject(Line(ax.coords_to_point(0, l+delta_l),ax.coords_to_point(9.5,l+delta_l),stroke_width = 1),num_dashes = 40)
		
		dlmdot = Dot(color = BLACK, radius = 0.001, stroke_width=0)
		dlmdot.move_to(ax.coords_to_point(0, l-delta_l), RIGHT)
		dlm_tex = MathTex(r'L-\varepsilon').next_to(dlmdot,LEFT).scale(0.5)
		dlm_line = DashedVMobject(Line(ax.coords_to_point(0, l-delta_l),ax.coords_to_point(9.5,l-delta_l),stroke_width = 1),num_dashes = 40)


		#Delta alpha
		a = 5
		delta_a = 0.5

		dapdot = Dot(color = BLACK, radius = 0.001, stroke_width=0)
		dapdot.move_to(ax.coords_to_point(a+delta_a, 0), UP)
		dap_tex = MathTex(r'a + \alpha').next_to(dapdot,DOWN).scale(0.4)
		dap_line = DashedVMobject(Line(ax.coords_to_point(a+delta_a, 0),ax.coords_to_point(a+delta_a,6.5),stroke_width = 1),num_dashes = 30)

		damdot = Dot(color = BLACK, radius = 0.001, stroke_width=0)
		damdot.move_to(ax.coords_to_point(a-delta_a, 0), UP)
		dam_tex = MathTex(r'a - \alpha').next_to(damdot,DOWN).scale(0.4)
		dam_line = DashedVMobject(Line(ax.coords_to_point(5-0.5, 0),ax.coords_to_point(a-delta_a,6.5),stroke_width = 1),num_dashes = 30)

		self.add(dapdot,dap_tex,dap_line,damdot,dam_tex,dam_line, dlpdot,dlp_tex,dlp_line,dlmdot,dlm_tex,dlm_line)