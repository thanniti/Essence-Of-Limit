#Limit##
from manim import*
import numpy as np
import math
import itertools

class Intro(Scene):
	def construct(self):
		#grid = NumberPlane()
		#self.basisofcal()
		self.quoteScene()
		#self.add(grid)
		self.Stacking()
		self.section()

	def quoteScene(self):
		quote1 = Tex("	If you disregard the very ","simplest cases",", there is in all of mathematics").scale(0.7)
		quote1_2 = Tex("not a single infinite series whose sum has been rigorously determined.").scale(0.7)
		quote1_3 = Tex("In other words,the most important parts of mathematics stand without").scale(0.7)
		quote1_4 = Tex("a foundation.").scale(0.7)

		quote_terminal = Tex("-Quoted in G F Simmons, Calculus Gems (New York 1992).").scale(0.7).set_color(TEAL)
		quote1.to_edge(UP)
		quote1[1].set_color(BLUE)
		quote1_2.next_to(quote1,DOWN)
		quote1_3.next_to(quote1_2,DOWN)
		quote1_4.next_to(quote1_3,DOWN).shift(4.5*LEFT)
		quote_terminal.next_to(quote1_3,3*DOWN)
		quote_end = VGroup(quote1_3, quote1_4)
		self.play(
			AnimationGroup(
				FadeIn(quote1, shift=RIGHT, run_time = 2),
				FadeIn(quote1_2, shift=RIGHT, run_time = 2),
				FadeIn(quote_end, shift=RIGHT, run_time = 2),
				lag_ratio = 0.8
				)
			)
		self.play(DrawBorderThenFill(quote_terminal), run_time = 4)
		self.wait()
		self.clear()
	def basisofcal(self):
		bubble = SVGMobject("Bubbles_thought").set_color(WHITE).scale(1.5)
		self.play(Create(bubble))

	def section(self):

		self.wait()
		section1_s = ImageMobject("stack").scale(0.15)
		rect_s = SurroundingRectangle(section1_s, buff=0.2)
		sec1 = Group(section1_s, rect_s)

		section2_s = ImageMobject("stack").scale(0.15)
		rect_s_2 = SurroundingRectangle(section2_s, buff=0.2)
		sec2 = Group(section2_s, rect_s_2)

		section3_s = ImageMobject("stack").scale(0.15)
		rect_s_3 = SurroundingRectangle(section3_s, buff=0.2)
		sec3 = Group(section3_s, rect_s_3)

		section4_s = ImageMobject("stack").scale(0.15)
		rect_s_4 = SurroundingRectangle(section4_s, buff=0.2)
		sec4 = Group(section4_s, rect_s_4)

		section5_s = ImageMobject("stack").scale(0.15)
		rect_s_5 = SurroundingRectangle(section1_s, buff=0.2)
		sec5 = Group(section5_s, rect_s_5)

		self.play(FadeIn(section1_s),Create(rect_s),lag_ratio=0.3)
		self.play(sec1.animate.shift(UP,2*LEFT))

		self.play(FadeIn(section2_s),Create(rect_s_2),lag_ratio=0.3)
		self.play(sec2.animate.shift(UP,2*RIGHT))

		self.play(FadeIn(section3_s),Create(rect_s_3),lag_ratio=0.3)
		self.play(sec3.animate.shift(1.5*DOWN,3.5*LEFT))

		self.play(FadeIn(section4_s),Create(rect_s_4),lag_ratio=0.3)
		self.play(sec4.animate.shift(1.5*DOWN))

		self.play(FadeIn(section5_s),Create(rect_s_5),lag_ratio=0.3)
		self.play(sec5.animate.shift(1.5*DOWN,3.5*RIGHT))

		self.wait(2)
		self.clear()


	def Stacking(self):
		edge1=Line([-4,-1,0],[0,-1,0])
		edge2=Line([0,-1,0],[0,-3,0])
		edge = VGroup(edge1,edge2)
		self.play(Write(edge))
		box1 = Rectangle(height=0.25, width=3.0,color = WHITE,fill_opacity=0.9)
		self.play(Create(box1))
		self.play(box1.animate.shift(0.85*DOWN))
		b1 = BraceBetweenPoints([0.2,-1,0],[1.3,-1,0])
		self.play(Write(b1))
		b1text = b1.get_tex("1").scale(0.5).shift(0.1*UP)
		self.play(Write(b1text))
		self.wait(2)
		self.play(FadeOut(b1),FadeOut(b1text))
		self.play(box1.animate.shift(0.25*UP))
		box2 = Rectangle(height=0.25, width=3.0,color = BLUE,fill_opacity=0.9).shift(1.5*LEFT+0.85*DOWN)
		self.play(FadeIn(box2, direction=3*RIGHT))
		self.wait()
		gbox1 = VGroup(box1,box2)
		gbox1.save_state()
		self.play(gbox1.animate.move_to(ORIGIN))
		dash = DashedVMobject(Line([0,-0.25,0],[0,0.25,0], color=YELLOW),num_dashes=5)
		self.play(Write(dash))
		text1 = Text("center of mass").next_to( dash, UP*0.75).scale(0.5)
		self.play(Write(text1))
		self.wait()
		text2 = Text("CM").next_to( dash, UP*0.75).scale(0.5)
		self.play(Transform(text1,text2))
		self.wait()
		self.play(FadeOut(dash),FadeOut(text1))
		self.play(Restore(gbox1))
		self.play(gbox1.animate.shift( 0.75*RIGHT))
		self.wait()
		b2 = BraceBetweenPoints([0.8,-1,0],[2.2,-1,0])
		b3 = BraceBetweenPoints([0.15,-1,0],[0.7,-1,0])
		self.play(GrowFromCenter(b2))
		b2text = b2.get_tex("1").scale(0.5).shift(0.1*UP)
		self.play(Write(b2text))
		self.play(GrowFromCenter(b3))
		b3text = b3.get_tex(r"\frac{1}{2}").scale(0.5).shift(0.3*UP)
		self.play(Write(b3text))
		self.wait()
		gb = VGroup(b2,b3,b3text,b2text)
		self.play(gbox1.animate.shift(0.25*UP))
		box3 = Rectangle(height=0.25, width=3.0,color = TEAL,fill_opacity=0.9).shift(1.5*LEFT+0.85*DOWN)
		self.play(FadeIn(box3, direction=3*RIGHT))
		gbox1.add(box3)
		self.play(gbox1.animate.shift((1/3)*RIGHT),gb.animate.shift((1/3)*RIGHT))

		b6 = BraceBetweenPoints([0.05,-1,0],[0.33,-1,0])
		b6text = b6.get_tex(r'\frac{1}{3}').scale(0.5).shift(0.3*UP)
		gb.add(b6)

		self.play(GrowFromCenter(b6))
		self.play(Write(b6text))
		gb.add(b6text)
		self.wait()

		self.play(gbox1.animate.shift(0.25*UP))
		box4 = Rectangle(height=0.25, width=3.0,color = GREEN,fill_opacity=0.9).shift(1.5*LEFT+0.85*DOWN)
		self.play(FadeIn(box4, shift=3*RIGHT))
		gbox1.add(box4)
		self.play(gbox1.animate.shift((1/4)*RIGHT),gb.animate.shift((1/4)*RIGHT))

		b7 = BraceBetweenPoints([0.025,-1,0],[0.25,-1,0])
		gb.add(b7)

		self.play(GrowFromCenter(b7))
		self.wait()

		self.play(gbox1.animate.shift(0.25*UP))
		box5 = Rectangle(height=0.25, width=3.0,color = YELLOW,fill_opacity=0.9).shift(1.5*LEFT+0.85*DOWN)
		self.play(FadeIn(box5, shift=3*RIGHT))
		gbox1.add(box5)
		self.play(gbox1.animate.shift((1/5)*RIGHT),gb.animate.shift((1/5)*RIGHT))

		b8 = BraceBetweenPoints([0.02,-1,0],[0.18,-1,0])
		gb.add(b8)

		self.play(GrowFromCenter(b8))
		bs = Text("How much block can we stack?").scale(0.5).to_edge(UP)
		self.play(FadeIn(bs))
		self.wait()

		self.play(gbox1.animate.shift(0.25*UP),run_time=0.1)
		box6 = Rectangle(height=0.25, width=3.0,color = GOLD,fill_opacity=0.9).shift(1.5*LEFT+0.85*DOWN)
		self.play(FadeIn(box6, shift=3*RIGHT),run_time=0.1)
		gbox1.add(box6)
		self.play(gbox1.animate.shift((1/6)*RIGHT),gb.animate.shift((1/6)*RIGHT),run_time=0.1)

		self.play(gbox1.animate.shift(0.25*UP),run_time=0.1)
		box7 = Rectangle(height=0.25, width=3.0,color = RED,fill_opacity=0.9).shift(1.5*LEFT+0.85*DOWN)
		self.play(FadeIn(box7, shift=3*RIGHT),run_time=0.1)
		gbox1.add(box7)
		self.play(gbox1.animate.shift((1/7)*RIGHT),gb.animate.shift((1/7)*RIGHT),run_time=0.1)

		self.play(gbox1.animate.shift(0.25*UP),run_time=0.1)
		box8 = Rectangle(height=0.25, width=3.0,color = MAROON,fill_opacity=0.9).shift(1.5*LEFT+0.85*DOWN)
		self.play(FadeIn(box8, shift=3*RIGHT),run_time=0.1)
		gbox1.add(box8)
		self.play(gbox1.animate.shift((1/8)*RIGHT),gb.animate.shift((1/8)*RIGHT),run_time=0.1)

		self.play(gbox1.animate.shift(0.25*UP),run_time=0.1)
		box9 = Rectangle(height=0.25, width=3.0,color = PURPLE,fill_opacity=0.9).shift(1.5*LEFT+0.85*DOWN)
		self.play(FadeIn(box9, shift=3*RIGHT),run_time=0.1)
		gbox1.add(box9)
		self.play(gbox1.animate.shift((1/9)*RIGHT),gb.animate.shift((1/9)*RIGHT),run_time=0.1)

		self.play(gbox1.animate.shift(0.25*UP),run_time=0.1)
		box10 = Rectangle(height=0.25, width=3.0,color = PINK,fill_opacity=0.9).shift(1.5*LEFT+0.85*DOWN)
		self.play(FadeIn(box10, shift=3*RIGHT),run_time=0.1)
		gbox1.add(box10)
		self.play(gbox1.animate.shift((1/10)*RIGHT),gb.animate.shift((1/10)*RIGHT),run_time=0.1)

		self.play(gbox1.animate.shift(0.25*UP),run_time=0.1)
		box11 = Rectangle(height=0.25, width=3.0,color = WHITE,fill_opacity=0.9).shift(1.5*LEFT+0.85*DOWN)
		self.play(FadeIn(box11, shift=3*RIGHT),run_time=0.1)
		gbox1.add(box11)
		self.play(gbox1.animate.shift((1/11)*RIGHT),gb.animate.shift((1/11)*RIGHT),run_time=0.1)

		self.play(gbox1.animate.shift(0.25*UP),run_time=0.1)
		box12 = Rectangle(height=0.25, width=3.0,color = TEAL,fill_opacity=0.9).shift(1.5*LEFT+0.85*DOWN)
		self.play(FadeIn(box12, shift=3*RIGHT),run_time=0.1)
		gbox1.add(box12)
		self.play(gbox1.animate.shift((1/12)*RIGHT),gb.animate.shift((1/12)*RIGHT),run_time=0.1)

		self.play(gbox1.animate.shift(0.25*UP),run_time=0.1)
		box13 = Rectangle(height=0.25, width=3.0,color = GREEN,fill_opacity=0.9).shift(1.5*LEFT+0.85*DOWN)
		self.play(FadeIn(box13, shift=3*RIGHT),run_time=0.1)
		gbox1.add(box13)
		self.play(gbox1.animate.shift((1/13)*RIGHT),gb.animate.shift((1/13)*RIGHT),run_time=0.1)

		bm = BraceBetweenPoints([0.5,-1,0],[4,-1,0])
		self.play(Transform(gb,bm))
		bmtext = bm.get_tex(r" 1",r"+",r"\frac{1}{2}",r"+",r"\frac{1}{3}",r"+",r"\frac{1}{4}",r"+",r"\frac{1}{5}",r"+",r"...").scale(0.4).shift(0.3*UP)
		self.play(Write(bmtext))
		self.wait()
#		bmtex2 = bm.get_tex(r'H_{n}').scale(0.7)
#		self.play(Transform(bmtext,bmtex2))
		self.wait(3)
#		self.play(FadeOut(gbox1),FadeOut(bm),FadeOut(bmtext))
		self.clear()

class SectionIntro(MovingCameraScene):

    def construct(self):
        self.camera.background_color = GREY_E
        self.add_title()
        self.show_thumbnails()
        # self.show_words()

    def add_title(self):
        title = Text("A Guide to").scale(1.2).to_corner(UR)
        title2 = Text("Sequence").scale(1.1).next_to(title,DOWN).to_edge(RIGHT)
        title3 = Text("and Series").scale(1.1).next_to(title2,DOWN).to_edge(RIGHT)
        title_group = VGroup(title, title2 ,title3)
        func = lambda pos: ((pos[0]*UR+pos[1]*LEFT) - pos)/3
        stream = StreamLines(func,opacity = 0.5)

        self.play(stream.create(), FadeIn(title_group))
        #self.add(title, title2, title3)

    def show_thumbnails(self):
        thumbnails = self.thumbnails = Group(
            Group(ScreenRectangle(stroke_width =2, stroke_color=WHITE, fill_opacity=1, fill_color = BLACK, color = WHITE)),
            Group(ScreenRectangle(stroke_width =2, stroke_color=WHITE, fill_opacity=1, fill_color = BLACK, color = WHITE)),
            Group(ScreenRectangle(stroke_width =2, stroke_color=WHITE, fill_opacity=1, fill_color = BLACK, color = WHITE)),
            Group(ScreenRectangle(stroke_width =2, stroke_color=WHITE, fill_opacity=1, fill_color = BLACK, color = WHITE)),
            Group(ScreenRectangle(stroke_width =2, stroke_color=WHITE, fill_opacity=1, fill_color = BLACK, color = WHITE)),
        )
        n = len(thumbnails)
        thumbnails.set_height(1.5)

        line = self.line = CubicBezier(
            [-5, 3, 0],
            [3, 3, 0],
            [-3, -3, 0],
            [5, -3, 0],
        )
        line.shift(MED_SMALL_BUFF * LEFT)
        for thumbnail, a in zip(thumbnails, np.linspace(0, 1, n)):
            thumbnail.move_to(line.point_from_proportion(a))
        dots = Tex("\\dots")
        dots.next_to(thumbnails[-1], RIGHT)

        self.add_phase_space_preview(thumbnails[0])
        self.add_heat_preview(thumbnails[1])
        self.add_fourier_series(thumbnails[2])
        self.add_matrix_exponent(thumbnails[3])
        self.add_laplace_symbol(thumbnails[4])

        self.play(
            Create(
                line,
                rate_func=lambda t: np.clip(t * (n + 1) / n, 0, 1)
            ),
            LaggedStart(*[
                GrowFromCenter(
                    thumbnail,
                    rate_func=squish_rate_func(
                        smooth,
                        0, 0.7,
                    )
                )
                for thumbnail in thumbnails
            ], lag_ratio=1),
            run_time=5
        )
        self.play(Write(dots))
        self.wait()

        self.thumbnails = thumbnails

    def add_phase_space_preview(self, thumbnail):
        mob = Tex(
            "Finite Sequence"
        ).set_color(PURPLE).set_sheen(-0.3, DR)
        mob.set_width(0.8 * thumbnail.get_width())
        mob.move_to(thumbnail)
        thumbnail.add(mob)

    def add_heat_preview(self, thumbnail):
        image = ImageMobject("pic_sec2_new")
        image.replace(thumbnail)
        thumbnail.add(image)

    def add_matrix_exponent(self, thumbnail):
        image = ImageMobject("pic_sec4_new")
        image.replace(thumbnail)
        thumbnail.add(image)

    def add_fourier_series(self, thumbnail):
        image = ImageMobject("pic_sec3_new")
        image.replace(thumbnail)
        thumbnail.add(image)

    def get_square_wave_approx(self, N, color):
        return FunctionGraph(
            lambda x: sum([
                (1 / n) * np.sin(n * PI * x)
                for n in range(1, 2 * N + 3, 2)
            ]),
            x_range=[0,2],
            color=color
        )

    def add_laplace_symbol(self, thumbnail):
        image = ImageMobject("pic_sec5_new")
        image.replace(thumbnail)
        thumbnail.add(image)


class Section1(Scene):
	def construct(self):
		#grid_1 = NumberPlane()
		#self.add(grid_1)
		#self.basicSequence()
		#self.spacificSequence()
		#self.showFormula()
		self.introtoSeries()
		#self.showFormula_for_series()
		#self.Geometric_formula()

	def basicSequence(self):
		sequence1 = MathTex(r"1",r",",r"4",r",",r"9",r",",r"16",r",",r"?")
		self.play(FadeIn(sequence1))
		self.wait(3)
		self.play(AnimationGroup(
			sequence1[0].animate.shift(4*LEFT,1.5*DOWN),
			sequence1[1].animate.shift(3*LEFT,1.5*DOWN),
			sequence1[2].animate.shift(2*LEFT,1.5*DOWN),
			sequence1[3].animate.shift(1*LEFT,1.5*DOWN),
			sequence1[4].animate.shift(1.5*DOWN),
			sequence1[5].animate.shift(1*RIGHT,1.5*DOWN),
			sequence1[6].animate.shift(2*RIGHT,1.5*DOWN),
			sequence1[7].animate.shift(3*RIGHT,1.5*DOWN),
			sequence1[8].animate.shift(4*RIGHT,1.5*DOWN),
			lag_ratio = 0
			)
		)
		###################################################################################
		rect = Rectangle(height=0.3, width=0.3, stroke_color = WHITE, stroke_opacity= 1)
		rect.set_fill(YELLOW, opacity=0.8)
		rect.set_stroke(width=0)

		rectgroup_1 = rect.copy().next_to(sequence1[0],5*UP)

		rgroup_2 = VGroup(*[rect.copy() for i in range(2)])
		rgroup_2.arrange(RIGHT, buff = 0.1)
		rectgroup_2 = VGroup(*[rgroup_2.copy() for i in range(2)])
		rectgroup_2.arrange(DOWN, buff = 0.1)
		rectgroup_2.next_to(sequence1[2],5*UP)

		rgroup_3 = VGroup(*[rect.copy() for i in range(3)])
		rgroup_3.arrange(RIGHT, buff = 0.1)
		rectgroup_3 = VGroup(*[rgroup_3.copy() for i in range(3)])
		rectgroup_3.arrange(DOWN, buff = 0.1)
		rectgroup_3.next_to(sequence1[4],5*UP)

		rgroup_4 = VGroup(*[rect.copy() for i in range(4)])
		rgroup_4.arrange(RIGHT, buff = 0.1)
		rectgroup_4 = VGroup(*[rgroup_4.copy() for i in range(4)])
		rectgroup_4.arrange(DOWN, buff = 0.1)
		rectgroup_4.next_to(sequence1[6],5*UP)
		
		rgroup_5 = VGroup(*[rect.copy() for i in range(5)])
		rgroup_5.arrange(RIGHT, buff = 0.1)
		rectgroup_5 = VGroup(*[rgroup_5.copy() for i in range(5)])
		rectgroup_5.arrange(DOWN, buff = 0.1)
		rectgroup_5.next_to(sequence1[8],5*UP)

		sequence1_25 = MathTex(r"25").shift(5*RIGHT,1.5*DOWN)

		sequence1_1 = MathTex(r"1^{1}").shift(5*LEFT,1.5*DOWN)
		sequence1_4 = MathTex(r"2^{2}").shift(2.5*LEFT,1.5*DOWN)
		sequence1_9 = MathTex(r"3^{3}").shift(1.5*DOWN)
		sequence1_16 = MathTex(r"4^{4}").shift(2.5*RIGHT,1.5*DOWN)

		b_1_up = MathTex(r"1").next_to(rectgroup_1, 0.5*UP)
		b_1_left = MathTex(r"1").next_to(rectgroup_1, 0.5*LEFT)

		b_2_up = MathTex(r"2").next_to(rectgroup_2[0], 0.5*UP)
		b_2_left = MathTex(r"2").next_to(rectgroup_2, 0.5*LEFT)

		b_3_up = MathTex(r"3").next_to(rectgroup_3[0], 0.5*UP)
		b_3_left = MathTex(r"3").next_to(rectgroup_3[1][0], LEFT)

		b_4_up = MathTex(r"4").next_to(rectgroup_4[0], 0.5*UP)
		b_4_left = MathTex(r"4").next_to(rectgroup_4, 0.5*LEFT)


		self.play(AnimationGroup(
			Create(rectgroup_1),
			Create(rectgroup_2),
			Create(rectgroup_3),
			Create(rectgroup_4),
			lag_ratio = 1
			)
		)
		self.wait(2)
		
		self.play(rectgroup_1.animate.set_color(GREEN))
		self.play(AnimationGroup(
			Write(b_1_up),
			Write(b_1_left),
			Transform(sequence1[0], sequence1_1)
			)
		)

		self.play(AnimationGroup(
			rectgroup_2[0][0].animate.set_color(GREEN),
			rectgroup_2[0][1].animate.set_color(GREEN),
			rectgroup_2[1][0].animate.set_color(GREEN),
			lag_ratio = 0
			)
		)
		self.play(AnimationGroup(
			Write(b_2_up),
			Write(b_2_left),
			Transform(sequence1[2], sequence1_4),
			)
		)

		self.play(AnimationGroup(
			rectgroup_3[0][0].animate.set_color(GREEN),
			rectgroup_3[0][1].animate.set_color(GREEN),
			rectgroup_3[0][2].animate.set_color(GREEN),
			rectgroup_3[1][0].animate.set_color(GREEN),
			rectgroup_3[2][0].animate.set_color(GREEN),
			)
		)
		self.play(AnimationGroup(
			Write(b_3_up),
			Write(b_3_left),
			Transform(sequence1[4], sequence1_9),
			)
		)

		self.play(AnimationGroup(
			rectgroup_4[0][0].animate.set_color(GREEN),
			rectgroup_4[0][1].animate.set_color(GREEN),
			rectgroup_4[0][2].animate.set_color(GREEN),
			rectgroup_4[0][3].animate.set_color(GREEN),
			rectgroup_4[1][0].animate.set_color(GREEN),
			rectgroup_4[2][0].animate.set_color(GREEN),
			rectgroup_4[3][0].animate.set_color(GREEN),
			)
		)
		self.play(AnimationGroup(
			Write(b_4_up),
			Write(b_4_left),
			Transform(sequence1[6], sequence1_16),
			)
		)


		self.play(Create(rectgroup_5))
		self.play(Transform(sequence1[8],sequence1_25))

		self.wait(3)
		self.clear()

	def spacificSequence(self):
		sequence_big = Text("Sequence", color = BLUE).scale(0.8)
		sequence_a = Text("Arithmetic Sequence").shift(3*LEFT).scale(0.7)
		sequence_b = Text("Geometric Sequence").shift(3*RIGHT).scale(0.7)

		partial_line_1 = Line([0,2.8,0],[0,1,0])
		partial_line_2 = Line([-3,1,0],[0,1,0])
		partial_line_3 = Line([0,1,0],[3,1,0])
		partial_line_4 = Line([-3,0.5,0],[-3,1,0])
		partial_line_5 = Line([3,0.5,0],[3,1,0])
		line_1 = VGroup(partial_line_4, partial_line_2, partial_line_1)
		line_2 = VGroup(partial_line_3, partial_line_5)

		self.play(FadeIn(sequence_big, scale = 5))
		self.wait(2)
		self.play(sequence_big.animate.to_edge(UP))

		self.play(Write(line_1))

		self.play(Write(sequence_a))
		self.wait(2)
		self.play(Write(line_2))
		self.play(Write(sequence_b))
		self.wait(3)

		self.play(AnimationGroup(
			FadeOut(line_2),
			FadeOut(line_1),
			FadeOut(sequence_b),
			FadeOut(sequence_big),
			)
		)
		self.play(sequence_a.animate.shift(3*RIGHT+3*UP))
		self.play(sequence_a.animate.set_color(BLUE))

		basis_a = MathTex(r"1",r",",r"5",r",",r"9",r",",r"13",r",",r"a_{5}")
		self.play(Write(basis_a))
		basis_a_answer = MathTex(r"17").shift(2*RIGHT)
		self.wait(2)
		self.play(AnimationGroup(
			basis_a[0].animate.shift(LEFT),
			basis_a[1].animate.shift(0.75*LEFT),
			basis_a[2].animate.shift(0.5*LEFT),
			basis_a[3].animate.shift(0.25*LEFT),
			#basis_a[4].animate.shift(),
			basis_a[5].animate.shift(0.25*RIGHT),
			basis_a[6].animate.shift(0.5*RIGHT),
			basis_a[7].animate.shift(0.75*RIGHT),
			basis_a[8].animate.shift(RIGHT),
			)
		)
		d_arrow_1 = CurvedArrow(np.array([-2.1,-0.3,0]),np.array([-1.2,-0.3,0])).scale(0.7)
		d_arrow_1_tex = MathTex(r"+4").next_to(d_arrow_1, 0.6*DOWN).scale(0.7)
		d_arrow_2 = CurvedArrow(np.array([-1.2,-0.3,0]),np.array([-0.2,-0.3,0])).scale(0.7)
		d_arrow_2_tex = MathTex(r"+4").next_to(d_arrow_2, 0.6*DOWN).scale(0.7)
		d_arrow_3 = CurvedArrow(np.array([-0.2,-0.3,0]),np.array([0.7,-0.3,0])).scale(0.7)
		d_arrow_3_tex = MathTex(r"+4").next_to(d_arrow_3, 0.6*DOWN).scale(0.7)
		d_arrow_4 = CurvedArrow(np.array([0.7,-0.3,0]),np.array([2,-0.3,0])).scale(0.7)
		d_arrow_4_tex = MathTex(r"+4").next_to(d_arrow_4, 0.6*DOWN).scale(0.7)
		d_arrow = VGroup(d_arrow_1,d_arrow_1_tex,d_arrow_2,d_arrow_2_tex,d_arrow_3,d_arrow_3_tex,d_arrow_4,d_arrow_4_tex)
		d_arrow_tex = VGroup(d_arrow_1_tex, d_arrow_2_tex, d_arrow_3_tex, d_arrow_4_tex)

		show_d = VGroup(d_arrow, basis_a)

		self.play(AnimationGroup(
			FadeIn(d_arrow_1),
			Write(d_arrow_1_tex),
			lag_ratio = 0.5,
			)
		)
		self.play(AnimationGroup(
			FadeIn(d_arrow_2),
			Write(d_arrow_2_tex),
			lag_ratio = 0.5,
			)
		)
		self.play(AnimationGroup(
			FadeIn(d_arrow_3),
			Write(d_arrow_3_tex),
			lag_ratio = 0.5,
			)
		)
		self.play(AnimationGroup(
			FadeIn(d_arrow_4),
			Write(d_arrow_4_tex),
			lag_ratio = 0.5,
			)
		)
		self.wait()
		self.play(Transform(basis_a[8], basis_a_answer))
		self.wait()

		d = MathTex(r"4",r"=",r"d").shift(UP)
		self.play(show_d.animate.shift(DOWN))
		self.play(TransformFromCopy(d_arrow_tex, d[0]))
		self.wait(2)
		self.play(AnimationGroup(
			FadeIn(d[1]),
			FadeIn(d[2]),
			)
		)

		self.wait()

		geo_sequence = Text("Geometric Sequence", color = BLUE).shift(3*UP).scale(0.7)

		self.play(AnimationGroup(
			FadeOut(d_arrow),
			FadeOut(basis_a),
			FadeOut(d),
			Transform(sequence_a, geo_sequence),
			)
		)
		basis_b = MathTex(r" 2 ",r",",r" 4 ",r",",r" 8 ",r",",r" 16 ",r",",r" a_{5} ")
		basis_b[0].shift(LEFT),
		basis_b[1].shift(0.75*LEFT),
		basis_b[2].shift(0.5*LEFT),
		basis_b[3].shift(0.25*LEFT),
		#basis_a[4].animate.shift(),
		basis_b[5].shift(0.25*RIGHT),
		basis_b[6].shift(0.5*RIGHT),
		basis_b[7].shift(0.75*RIGHT),
		basis_b[8].shift(RIGHT),

		a_arrow_1 = CurvedArrow(np.array([-2.1,-0.3,0]),np.array([-1.2,-0.3,0])).scale(0.7)
		a_arrow_1_tex = MathTex(r"\times 2").next_to(a_arrow_1, 0.6*DOWN).scale(0.7)
		a_arrow_2 = CurvedArrow(np.array([-1.2,-0.3,0]),np.array([-0.2,-0.3,0])).scale(0.7)
		a_arrow_2_tex = MathTex(r"\times 2").next_to(a_arrow_2, 0.6*DOWN).scale(0.7)
		a_arrow_3 = CurvedArrow(np.array([-0.2,-0.3,0]),np.array([0.7,-0.3,0])).scale(0.7)
		a_arrow_3_tex = MathTex(r"\times 2").next_to(a_arrow_3, 0.6*DOWN).scale(0.7)
		a_arrow_4 = CurvedArrow(np.array([0.7,-0.3,0]),np.array([2,-0.3,0])).scale(0.7)
		a_arrow_4_tex = MathTex(r"\times 2").next_to(a_arrow_4, 0.6*DOWN).scale(0.7)
		a_arrow = VGroup(a_arrow_1,a_arrow_1_tex,a_arrow_2,a_arrow_2_tex,a_arrow_3,a_arrow_3_tex,a_arrow_4,a_arrow_4_tex)
		a_arrow_tex = VGroup(a_arrow_1_tex, a_arrow_2_tex, a_arrow_3_tex, a_arrow_4_tex)

		show_r = VGroup(a_arrow, basis_b)

		basis_r_answer = MathTex(r"32").shift(2*RIGHT)

		self.play(FadeIn(basis_b))

		self.play(AnimationGroup(
			FadeIn(a_arrow_1),
			Write(a_arrow_1_tex),
			lag_ratio = 0.5,
			)
		)
		self.play(AnimationGroup(
			FadeIn(a_arrow_2),
			Write(a_arrow_2_tex),
			lag_ratio = 0.5,
			)
		)
		self.play(AnimationGroup(
			FadeIn(a_arrow_3),
			Write(a_arrow_3_tex),
			lag_ratio = 0.5,
			)
		)
		self.play(AnimationGroup(
			FadeIn(a_arrow_4),
			Write(a_arrow_4_tex),
			lag_ratio = 0.5,
			)
		)
		self.wait()
		self.play(Transform(basis_b[8], basis_r_answer))

		r = MathTex(r"2",r"=",r"r").shift(UP)
		self.play(show_r.animate.shift(DOWN))
		self.play(TransformFromCopy(a_arrow_tex, r[0]))
		self.wait(2)
		self.play(AnimationGroup(
			FadeIn(r[1]),
			FadeIn(r[2]),
			)
		)

		self.wait(3)

		self.clear()

	def showFormula(self):
		
		b_rect = Rectangle(height=5, width=8).shift(0.5*DOWN)

		formula = Tex("Formula", color = BLUE).next_to(b_rect,1.5*UP)

		a_s_f = Tex("-Arithmetic sequence").scale(0.8).shift(UP,1.5*LEFT)
		formula_a = MathTex(r"a_{n} = a_{1}+(n-1)d").scale(0.8).next_to(a_s_f, DOWN)

		g_s_f = Tex("-Geometric Sequence").scale(0.8).shift(DOWN, 1.5*LEFT)
		formula_g = MathTex(r"a_{n} = a_{1}r^{n-1}").scale(0.8).next_to(g_s_f, DOWN)

		self.play(FadeIn(formula),Create(b_rect))
		self.play(AnimationGroup(
			FadeIn(a_s_f),
			FadeIn(formula_a),
			lag_ratio =1,
			)
		)
		self.wait()
		self.play(AnimationGroup(
			FadeIn(g_s_f),
			FadeIn(formula_g),
			lag_ratio =1,
			)
		)
		self.wait()
		self.clear()

	def introtoSeries(self):
		basis_a_again = MathTex(r"1",r",",r"5",r",",r"9",r",",r"13",r",",r"17",r",",r"...",r",",r"a_{n}")
		basis_a_again_series = MathTex(r"1",r"+",r"5",r"+",r"9",r"+",r"13",r"+",r"17",r"+",r"...",r"+",r"a_{n}")

		s_head = Text("The sum of the terms of a sequence is called a 'series'").scale(0.6).to_edge(UP)

		sigma = MathTex(r"S_{n}",r"=",r"\sum_{n=1}^{n}",r"a_{n}").shift(0.5*DOWN)

		self.play(FadeIn(basis_a_again))
		self.wait()
		self.play(AnimationGroup(
			Transform(basis_a_again, basis_a_again_series),
			)
		)
		self.play(Write(s_head))
		self.wait(2)
		self.play(AnimationGroup(
			basis_a_again_series.animate.shift(2.5*UP),
			FadeOut(basis_a_again),
			FadeOut(s_head),
			)
		)
		self.wait()
		plus_group = VGroup(
			basis_a_again_series[1],
			basis_a_again_series[3],
			basis_a_again_series[5],
			basis_a_again_series[7],
			basis_a_again_series[9],
			basis_a_again_series[11],
			)
		a_n_group = VGroup(
			basis_a_again_series[0],
			basis_a_again_series[2],
			basis_a_again_series[4],
			basis_a_again_series[6],
			basis_a_again_series[8],
			basis_a_again_series[12],
			)

		self.play(AnimationGroup(
			TransformFromCopy(plus_group,sigma[2]),
			run_time = 1.5
			)
		)

		self.wait(2)
		self.play(TransformFromCopy(a_n_group,sigma[3], run_time = 1.5))

		self.wait()
		self.play(AnimationGroup(
			FadeIn(sigma[0]),
			FadeIn(sigma[1]),
			lag_ratio = 0
			)
		)

		self.play(Indicate(sigma[0]), run_time = 4)
		self.play(AnimationGroup(
			Indicate(sigma[2]),
			Indicate(basis_a_again_series[1]),
			Indicate(basis_a_again_series[3]),
			Indicate(basis_a_again_series[5]),
			Indicate(basis_a_again_series[7]),
			Indicate(basis_a_again_series[9]),
			Indicate(basis_a_again_series[11]),
			run_time = 4,
			lag_ratio = 0,
			)
		)
		#self.play(Indicate(sigma[2]), run_time = 3)
		self.play(Indicate(sigma[3]), run_time = 4)

		self.wait(2)
		self.clear()

	def showFormula_for_series(self):
		s_rect = Rectangle(height=5, width=8).shift(0.5*DOWN)

		formula = Tex(r"Arithmetic Series", color = BLUE).next_to(s_rect,1.5*UP)

		formula_a_s = MathTex(r"S_{n}=\frac{n}{2}[2a_{1}+(n-1)d]").scale(0.8).shift(UP)

		formula_g_s = MathTex(r"S_{n}=\frac{n}{2}(a_{1}+a_{n})").scale(0.8).next_to(formula_a_s,3.5*DOWN)

		self.play(FadeIn(formula),Create(s_rect))
		self.play(AnimationGroup(
			FadeIn(formula_a_s),
			lag_ratio =1,
			)
		)
		self.wait()
		self.play(AnimationGroup(
			FadeIn(formula_g_s),
			lag_ratio =1,
			)
		)
		self.wait()

	def Geometric_formula(self):
		g_rect = Rectangle(height=5, width=8).shift(0.5*DOWN)

		formula = Tex("Geometric Series", color = BLUE).next_to(g_rect,1.5*UP)

		g_formula = Tex("When r > 1",color = YELLOW).scale(0.8).shift(UP,1.5*LEFT)
		g_f_1 = MathTex(r"S_{n}=a_{1}(\frac{r^{n}-1}{r-1})").scale(0.8).next_to(g_formula, DOWN)
		g_g_1 = VGroup(g_formula, g_f_1)
		rect_g_1 = SurroundingRectangle(g_g_1, color = BLUE)

		g_1_formula = Tex("When r < 1", color = YELLOW).scale(0.8).shift(DOWN, 1.5*LEFT)
		g_f_2 = MathTex(r"S_{n}=a_{1}(\frac{1-r^{n}}{1-r})").scale(0.8).next_to(g_1_formula, DOWN)
		g_g_2 = VGroup(g_1_formula, g_f_2)
		rect_g_2 = SurroundingRectangle(g_g_2, color = BLUE)

		g_f_3 = MathTex(r"S_{n}=\frac{a_{n}r-a_{1}}{1r-1}").scale(0.8).shift(1.7*RIGHT,0.5*DOWN)
		rect_g_f_3 = SurroundingRectangle(g_f_3)
		

		self.play(FadeIn(formula),Create(g_rect))
		self.play(AnimationGroup(
			FadeIn(g_formula),
			FadeIn(g_f_1),
			Create(rect_g_1),
			lag_ratio =1,
			)
		)
		self.wait()
		self.play(AnimationGroup(
			FadeIn(g_1_formula),
			FadeIn(g_f_2),
			Create(rect_g_2),
			lag_ratio =1,
			)
		)
		self.wait()
		self.play(FadeIn(g_f_3))
		self.play(Create(rect_g_f_3))
		self.clear()
		self.wait(5)


	

class Section2(MovingCameraScene):
	
	def construct(self):
		#limit_nuberplane = NumberPlane()
		#self.add(limit_nuberplane)
		#self.infiniteSeries()
		#self.show_infinite_sigma()
		self.Div_Conv()
		#self.example_test()
		#self.Sinusodial()

	def infiniteSeries(self):
		bubble = SVGMobject("Bubbles_thought", color = WHITE).scale(4.5).shift(DOWN)
		another_ways = Text("what about when n is infinite",color=BLACK).scale(0.7)
		self.play(FadeIn(bubble))
		self.play(Write(another_ways))
		self.wait(2)
		self.clear()

		

	def show_infinite_sigma(self):
		tex0 = MathTex(r"\sum_{n=1}^{\infty }\frac{1}{n} =",r" 1",r"+",r"\frac{1}{2}",r"+",r"\frac{1}{3}",r"+",r"\frac{1}{4}",r"+",r"\frac{1}{5}",r"+",r"...").scale(0.8).shift(2.5*UP)
		infinite_sigma = MathTex(r"S_{\infty }=\sum_{n=1}^{\infty }a_{n}",r"=",r"\lim_{n\to\infty }",r"S_{n}").scale(0.8)
		rect_indicate = SurroundingRectangle(infinite_sigma[2])
		arrow_limit = Arrow([1.1,-0.15,0],[1.1,-1.5,0], color = YELLOW)
		limit_text = Text("limit of n approce infinite", color = YELLOW).scale(0.5).next_to(arrow_limit, 0.5*DOWN)
		self.play(FadeIn(tex0))
		self.play(AnimationGroup(
			FadeIn(infinite_sigma)
			)
		)
		self.play(Write(rect_indicate), run_time=0.5)
		self.play(GrowArrow(arrow_limit))
		self.play(FadeIn(limit_text))

		self.wait(3)

		self.clear()

	def Div_Conv(self):
		
		sequence_div = MathTex(r"\frac{1}{2}",r",",r"2",r",",r"\frac{9}{2}",r",",r"8",r",",r"...")
		sequence_div[0].shift(1*LEFT)
		sequence_div[1].shift(0.75*LEFT)
		sequence_div[2].shift(0.5*LEFT)
		sequence_div[3].shift(0.25*LEFT)
		sequence_div[5].shift(0.25*RIGHT)
		sequence_div[6].shift(0.5*RIGHT)
		sequence_div[7].shift(0.75*RIGHT)
		sequence_div[8].shift(1*RIGHT)


		ax = Axes(x_range=[-1,10,2], y_range = [-1,10,2],axis_config={"include_numbers": True}).scale(0.8)
		new_axes = Axes(x_range=[-1,10,2], x_length = 12, y_range = [-5,10,2]).scale(0.8)
		new_axes_conv = Axes(x_range=[-1,100,2], x_length = 120, y_range = [-5,10,2], x_axis_config={"numbers_to_include": [94,96,98,100]},).scale(0.8).shift(43.125*RIGHT)

		def function(x):
			return 0.5*x**2

		graph_1 = ax.get_graph(function , x_range = [0 ,4.5], stroke_width = 1.7).set_color(TEAL)
		graph_2 = new_axes.get_graph(lambda x: 3*np.sin(5*x)/x, x_range = [0.35 ,9], stroke_width = 1.7).set_color(TEAL)
		graph_2_conv = new_axes_conv.get_graph(lambda x: 3*np.sin(5*x)/x, x_range = [0.35 ,99], stroke_width = 2.5).set_color(TEAL)

		k1 = ValueTracker(0.35)
		#k2 = ValueTracker()
		k = ValueTracker(-3)



		dot_moving_conv = always_redraw(lambda: Dot().move_to(
					new_axes.c2p(k1.get_value(), graph_2.underlying_function(k1.get_value()))
				)
			)

		h_tex = MathTex(r"a_{n}:").shift(1.5*UP).scale(0.8)

		moving_conv_line = always_redraw(
			lambda: new_axes.get_vertical_line(
					new_axes.i2gp(k1.get_value(), graph_2),
					color = YELLOW
				)
			)

		h_conv_value = DecimalNumber(num_decimal_places=2).next_to(h_tex,RIGHT,buff =0.2).set_color(YELLOW)
		h_conv_value.add_updater(lambda d: d.set_value(moving_conv_line.height))

		value = VGroup(h_tex, h_conv_value)
		rect_value = SurroundingRectangle(value)
		h_tex_d = Text("decrease").next_to(rect_value, 0.6*UP)
		h_tex_d.scale(0.6)

		moving_slope = always_redraw(
			lambda: ax.get_secant_slope_group(
				x = k.get_value(),
				graph = graph_1,
				dx = 0.05,
				secant_line_length = 4,
				secant_line_color = YELLOW,
				)
		)

		dot_conv = Dot(new_axes_conv.i2gp(graph_2_conv.t_max, graph_2_conv),radius = 0)


		slope_value_text = (
			Tex("Slope value: ")
			.next_to(ax, DOWN, buff = 0.1)
			.set_color(YELLOW)
			.add_background_rectangle()
		)


		slope_value = always_redraw(
			lambda: DecimalNumber(num_decimal_places=1)
			.set_value(graph_1.underlying_function(k.get_value()))
			.next_to(slope_value_text, RIGHT, buff = 0.1)
			.set_color(YELLOW)
		).add_background_rectangle()


		self.play(FadeIn(sequence_div))
		self.wait()
		self.play(AnimationGroup(
			sequence_div.animate.to_edge(DOWN),
			lag_ratio = 0,
			)
		)
		self.play(sequence_div.animate.scale(0.7))
		self.play(Create(ax))

		dot_div_group = VGroup()
		for x in range (1, 5):
			dot_div = Dot(ax.c2p(x,0.5*x**2,0), radius = 0.03, color = YELLOW)
			dot_div_group.add(dot_div)
			#self.play(Create(dot_div), run_time = 0.7)
			self.play(AnimationGroup(
				Create(dot_div),
				run_time = 0.7,
				lag_ratio = 1 ,
				)
			)


		self.play(FadeOut(sequence_div))
		self.wait()

		self.play(Write(graph_1))
		
		#self.add(moving_slope, slope_value, slope_value_text, dot)
		#self.play(k.animate.set_value(3), run_time = 10, rate_func = linear)
		
		self.wait()

		#div_tex = Text('diverge to infinite', color = BLUE).scale(0.5).next_to(graph_1, 0.5*RIGHT , buff = 0.7)
		div_tex_2 = Text('"Divergent"', color = BLUE).scale(0.5).next_to(graph_1, 0.5*RIGHT)

		#self.play(FadeIn(div_tex))
		#self.wait()
		self.play(FadeIn(div_tex_2))
		self.wait()

		self.play(AnimationGroup(
			FadeOut(graph_1),
			FadeOut(dot_div_group),
			#FadeOut(div_tex),
			FadeOut(div_tex_2),
			lag_ratio = 0
			)
		)

		self.play(ReplacementTransform(ax, new_axes))
		self.play(Write(graph_2))
		self.wait()
		self.play(Create(dot_moving_conv),Create(moving_conv_line),Write(h_conv_value),Write(h_tex),lag_ratio=0)

		self.play(k1.animate.set_value(9), run_time = 7 ,rate_func = rate_functions.ease_in_out_cubic)
		self.play(Create(rect_value),Write(h_tex_d),lag_ratio = 0.5)

		div_tex_3 = Text('"converge to zero"', color = BLUE).scale(0.7).next_to(dot_conv,DOWN,buff =1)

		self.wait(2)
		self.play(AnimationGroup(
			FadeOut(dot_moving_conv),
			FadeOut(moving_conv_line),
			FadeOut(h_conv_value),
			FadeOut(h_tex),
			FadeOut(rect_value),
			FadeOut(h_tex_d),
			lag_ratio = 0
			)
		)

		self.play(AnimationGroup(
			Transform(new_axes, new_axes_conv),
			Transform(graph_2, graph_2_conv),
			lag_ratio = 0
			)
		)
		#self.play(ReplacementTransform(dot_moving_conv, dot_conv))
		self.wait(2)
		self.play(self.camera.frame.animate.move_to(dot_conv), run_time = 8)
		self.wait()
		self.play(FadeIn(div_tex_3))

		self.wait(2)
		self.clear()


class Section2_Ex(ZoomedScene):
	def __init__(self, **kwargs):
		ZoomedScene.__init__(
			self,
			zoom_factor=0.3,
			zoomed_display_height=3,
			zoomed_display_width=4,
			image_frame_stroke_width=15,
			zoomed_camera_config={
				"default_frame_stroke_width": 3,
				},
			**kwargs
		)
	def construct(self):
		self.example_test()	

	def example_test(self):

		k = ValueTracker(0.2)
		k3 = ValueTracker(0.245)

		ex = Tex("Some Simple Examples").scale(1.2)

		ex_1 = MathTex(r"a_{n}=",r"2",color = BLUE).next_to(ex, 2*LEFT+3.5*UP)
		ex_2 = MathTex(r"a_{n}=-3n", color = BLUE).next_to(ex, 2*RIGHT+3.5*UP)
		ex_3 = MathTex(r"a_{n}=\frac{1}{n}+1", color = BLUE).next_to(ex, 2*LEFT+3.5*DOWN)
		ex_4 = MathTex(r"a_{n}=(-1)^{n}", color = BLUE).next_to(ex, 2*RIGHT+3.5*DOWN)

		ex_2_new =  MathTex(r"a_{n}=-3n", color = BLUE).to_edge(UP)
		ex_3_new = MathTex(r"a_{n}=\frac{1}{n}+1", color = BLUE).to_edge(UP)
		ex_4_new = MathTex(r"a_{n}=(-1)^{n}", color = BLUE).to_edge(UP)

		ex_1_text = MathTex(r"2",r",",r"2",r",",r"2",r",",r"2",r",",r"...").shift(1.5*UP)
		ex_1_a_1 = MathTex(r"a_{1}=",r"2").shift(3*LEFT+1.5*UP)
		ex_1_a_2 = MathTex(r"a_{2}=",r"2").shift(1*LEFT+1.5*UP)\




		ex_1_a_3 = MathTex(r"a_{3}=",r"2").shift(1*RIGHT+1.5*UP)
		ex_1_a_4 = MathTex(r"a_{4}=",r"2").shift(3*RIGHT+1.5*UP)
		ex_1_a = VGroup(ex_1_a_1, ex_1_a_2, ex_1_a_3, ex_1_a_4)

		ex_1_infinite = MathTex(r"\lim_{n\to\infty }a_{n} = 2").scale(0.8)
		ex_1_rect = SurroundingRectangle(ex_1_infinite).shift(2*LEFT)
		ex_1_arrow = Arrow([-1.13,0,0],  [1,0,0], color = YELLOW)
		ex_1_conv = Text("Convergent", color = YELLOW).scale(0.7).next_to(ex_1_arrow, RIGHT)

		ex_2_ax = Axes(x_range=[-0.5,5,1],y_range=[-10,1,1], x_axis_config={"include_numbers": True}, y_axis_config={"numbers_to_include": [-3, -6, -9]}, tips=False)
		ex_2_graph = ex_2_ax.get_graph(lambda x: -3*x , x_range = [0,3.2],color = BLUE , stroke_width = 1.5)
		
		ex_3_ax = Axes(x_range=[-1,6,0.5],y_range=[-1,7,1], y_axis_config={"numbers_to_include": [1]},tips=False)
		ex_3_graph = ex_3_ax.get_graph(lambda x: (1/x)+1, x_range = [0.2,5] , color = GREEN)
		ex_3_epsintobe = DashedVMobject(Line(ex_3_ax.c2p(0,1,0),ex_3_ax.c2p(5,1,0)))
		#ex_3_graph_new = ex_3_ax.get_graph(lambda x: (1/x)+1, x_range = [0.25, 5], color = RED)
		ex_3_graph_tex = ex_2_ax.get_graph_label(ex_3_graph,r"\frac{1}{n}+1",x_val=0.2, direction=UP / 2).shift(RIGHT).scale(0.6)
		#ex_3_graph_tex_new = MathTex(r"\frac{1}{n}+n").next_to(ex_3_graph, RIGHT).scale(0.6)
		ex_3_graph_g1 = VGroup(ex_3_graph, ex_3_graph_tex)

		ex_3_dot_move = always_redraw(lambda: Dot().move_to(
					ex_3_ax.c2p(k.get_value(), ex_3_graph.underlying_function(k.get_value()))
				)
			)

		ex_3_conv = Text("Converge to 1").scale(0.6)

		ex_4_ax = Axes(
			x_range=[-1,6,1],
			y_range=[-2,2,1],
			x_axis_config={"numbers_to_include": [2, 4, 6], "label_direction": DOWN},
			y_axis_config={"numbers_to_include": [-1, 1]},
			tips=False
			)

		#ex_4_graph = ex_4_ax.get_graph(lambda x: -1.55*np.sin(x) , x_range=[0,5.5], color=GREEN)
		line_1 = DashedLine(ex_4_ax.c2p(-1,-1,0),ex_4_ax.c2p(5.5,-1,0),color=GRAY)
		line_2 = DashedLine(ex_4_ax.c2p(-1,1,0),ex_4_ax.c2p(5.5,1,0),color=GRAY)
	
		ex_2_dot_1_p = ex_2_ax.c2p(1,-3)
		ex_2_dot_2_p = ex_2_ax.c2p(2,-6)
		ex_2_dot_3_p = ex_2_ax.c2p(3,-9)

		ex_2_dot_1 = Dot(ex_2_ax.c2p(1,0), color=YELLOW, radius = 0.04)
		ex_2_dot_2 = Dot(ex_2_ax.c2p(2,0), color=YELLOW, radius = 0.04)
		ex_2_dot_3 = Dot(ex_2_ax.c2p(3,0), color=YELLOW, radius = 0.04)

		self.play(FadeIn(ex))
		self.wait()
		self.play(AnimationGroup(
			TransformFromCopy(ex, ex_1),
			TransformFromCopy(ex, ex_2),
			TransformFromCopy(ex, ex_3),
			TransformFromCopy(ex, ex_4),
			lag_ratio = 0.4,
			)
		)
		self.wait(2)
		self.play(AnimationGroup(
			FadeOut(ex),
			FadeOut(ex_2),
			FadeOut(ex_3),
			FadeOut(ex_4),
			)
		)

		self.wait(2)
		self.play(ex_1.animate.shift(4*RIGHT+2*UP))

		self.play(AnimationGroup(
			FadeIn(ex_1_a_1[0]),
			FadeIn(ex_1_a_2[0]),
			FadeIn(ex_1_a_3[0]),
			FadeIn(ex_1_a_4[0]),
			lag_ratio = 0,
			)
		)


		self.play(AnimationGroup(
			TransformFromCopy(ex_1[1], ex_1_a_1[1]),
			TransformFromCopy(ex_1[1], ex_1_a_2[1]),
			TransformFromCopy(ex_1[1], ex_1_a_3[1]),
			TransformFromCopy(ex_1[1], ex_1_a_4[1]),
			lag_ratio = 1.5,
			)
		)
		self.wait()
		self.play(ReplacementTransform(ex_1_a, ex_1_text))

		self.wait()
		self.play(FadeIn(ex_1_infinite))
		self.wait(2)
		self.play(ex_1_infinite.animate.shift(2*LEFT))

		self.play(AnimationGroup(
			Create(ex_1_rect),
			GrowArrow(ex_1_arrow),
			lag_ratio = 0.2
			)
		)
		self.play(Write(ex_1_conv))

		self.wait()

		self.play(FadeOut(ex_1_text),FadeOut(ex_1_a),FadeOut(ex_1_infinite),FadeOut(ex_1_rect),FadeOut(ex_1_arrow),FadeOut(ex_1_conv))
		e = ValueTracker(0)
		ex1_ax = Axes(x_range = [-1,5,1],y_range=[-1,3.5,1],tips=False, y_axis_config={"numbers_to_include": [2]})
		ex1_graph = Line(ex1_ax.c2p(-1,2,0),ex1_ax.c2p(4.5,2,0),color=BLUE)
		ex1_dot = Dot(ex1_ax.c2p(-1,2,0),color=YELLOW)
		ex_1_tex = Tex("always equals 2").shift(DOWN)

		self.play(Create(ex1_ax))
		self.bring_to_back(ex1_graph)
		self.play(Create(ex1_graph))
		self.play(Create(ex1_dot),Write(ex_1_tex))
		self.play(ex1_dot.animate.move_to(ex1_ax.c2p(4.5,2,0)), run_time = 3)

		
		self.wait(2)
		self.play(FadeOut(ex1_ax),FadeOut(ex1_dot),FadeOut(ex_1_tex),FadeOut(ex1_graph))

		self.play(ReplacementTransform(ex_1 ,ex_2_new))
		self.play(Create(ex_2_ax))

		self.wait()

		self.play(AnimationGroup(
			FadeIn(ex_2_dot_1),
			FadeIn(ex_2_dot_2),
			FadeIn(ex_2_dot_3),
			lag_ratio = 0.4
			)
		)
		self.play(AnimationGroup(
			ex_2_dot_1.animate.move_to(ex_2_dot_1_p),
			ex_2_dot_2.animate.move_to(ex_2_dot_2_p),
			ex_2_dot_3.animate.move_to(ex_2_dot_3_p),
			lag_ratio = 0.4
			)
		)
		self.play(Write(ex_2_graph))

		self.wait()

		ex_2_div = Text("Divergent", color = YELLOW).shift(0.8*RIGHT).scale(0.7)

		self.play(Write(ex_2_div))

		self.wait(2)

		self.play(AnimationGroup(
			ReplacementTransform(ex_2_new, ex_3_new),
			FadeOut(ex_2_div),
			#FadeOut(ex_2_graph),
			#FadeOut(ex_2_ax),
			FadeOut(ex_2_dot_1),
			FadeOut(ex_2_dot_2),
			FadeOut(ex_2_dot_3),
			lag_ratio = 0,
			)
		)
		self.play(AnimationGroup(
			ReplacementTransform(ex_2_ax,ex_3_ax),
			ReplacementTransform(ex_2_graph, ex_3_graph_g1),
			#Write(ex_3_graph_tex),
			lag_ratio = 0,
			)
		)
		self.play(Write(ex_3_epsintobe))
		self.wait()

		self.play(Create(ex_3_dot_move))
		self.play(Write(ex_3_conv))
		self.play(k.animate.set_value(5), run_time = 5 , rate_funcr = linear)
		self.wait()

		self.play(AnimationGroup(
			ReplacementTransform(ex_3_new, ex_4_new),
			ReplacementTransform(ex_3_ax, ex_4_ax),
			FadeOut(ex_3_epsintobe),
			FadeOut(ex_3_graph_g1),
			FadeOut(ex_3_dot_move),
			FadeOut(ex_3_conv),
			)
		)

		ex_4_div = Tex('Divergent', color = YELLOW).shift(RIGHT,1.9*UP).add_background_rectangle()
		for i in range(0,5,2):
			ex_4_dot_1 = Dot(ex_4_ax.c2p(i,1), color = YELLOW, radius=0.05)
			self.play(FadeIn(ex_4_dot_1))
		for i in range(1,6,2):
			ex_4_dot_2 = Dot(ex_4_ax.c2p(i,-1), color = YELLOW, radius=0.05)
			self.play(FadeIn(ex_4_dot_2))
		

		self.wait()
		self.play(Create(line_1),Create(line_2))
		self.bring_to_back(line_1)
		self.bring_to_back(line_2)
		self.wait()
		#self.play(Create(ex_4_graph))
		self.wait()
		self.play(FadeIn(ex_4_div))

		self.wait(2)
		self.clear()
		self.wait(5)
	

	def Sinusodial(self):
		self.show_axis()
		self.show_circle()
		self.move_dot_and_draw_curve()
		self.wait()

	def show_axis(self):
		x_start = np.array([-6,0,0])
		x_end = np.array([6,0,0])

		y_start = np.array([-4,-2,0])
		y_end = np.array([-4,2,0])

		x_axis = Line(x_start, x_end)
		y_axis = Line(y_start, y_end)

		self.add(x_axis, y_axis)
		self.add_x_labels()

		self.origin_point = np.array([-4,0,0])
		self.curve_start = np.array([-3,0,0])

	def add_x_labels(self):
		x_labels = [
			MathTex(r"\pi"), MathTex(r"2 \pi"),
			MathTex(r"3 \pi"), MathTex(r"4 \pi"),
		]

		for i in range(len(x_labels)):
			x_labels[i].next_to(np.array([-1 + 2*i, 0, 0]), DOWN)
			self.add(x_labels[i])

	def show_circle(self):
		circle = Circle(radius=1)
		circle.move_to(self.origin_point)
		self.add(circle)
		self.circle = circle

	def move_dot_and_draw_curve(self):
		orbit = self.circle
		origin_point = self.origin_point

		dot = Dot(radius=0.08, color=YELLOW)
		dot.move_to(orbit.point_from_proportion(0))
		self.t_offset = 0
		rate = 0.25

		def go_around_circle(mob, dt):
			self.t_offset += (dt * rate)
			# print(self.t_offset)
			mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

		def get_line_to_circle():
			return Line(origin_point, dot.get_center(), color=BLUE)

		def get_line_to_curve():
			x = self.curve_start[0] + self.t_offset * 4
			y = dot.get_center()[1]
			return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )


		self.curve = VGroup()
		self.curve.add(Line(self.curve_start,self.curve_start))
		def get_curve():
			last_line = self.curve[-1]
			x = self.curve_start[0] + self.t_offset * 4
			y = dot.get_center()[1]
			new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
			self.curve.add(new_line)

			return self.curve

		dot.add_updater(go_around_circle)

		origin_to_circle_line = always_redraw(get_line_to_circle)
		dot_to_curve_line = always_redraw(get_line_to_curve)
		sine_curve_line = always_redraw(get_curve)

		self.add(dot)
		self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
		self.wait(8.5)

		dot.remove_updater(go_around_circle)

        #self.play(AnimationGroup(
        	#FadeOut(circle),
        	#)
       # )

class Section3(Scene):

	EXPO_COLOR = [RED,ORANGE,GOLD,YELLOW,GREEN,TEAL,BLUE,PURPLE,PINK,LIGHT_PINK]

	def construct(self):
		#s3_grid = NumberPlane()
		#self.add(s3_grid)
		self.showproperty()
		self.property_ex()
		self.property_extra()
		#self.there_are_4_ways()
		#self.wait(5)

	def showproperty(self):

		equa_num_1 = Tex("1.").shift(5.5*LEFT+2.2*UP).scale(0.8)
		equa_num_2 = Tex("2.").scale(0.8).next_to(equa_num_1, 1.6*DOWN)
		equa_num_3 = Tex("3.").scale(0.8).next_to(equa_num_2, 1.6*DOWN)
		equa_num_4 = Tex("4.").scale(0.8).next_to(equa_num_3, 1.6*DOWN)
		equa_num_5 = Tex("5.").scale(0.8).next_to(equa_num_4, 1.6*DOWN)
		equa_num_6 = Tex("6.").scale(0.8).next_to(equa_num_5, 1.6*DOWN)
		equa_num_7 = Tex("7.").scale(0.8).next_to(equa_num_6, 1.6*DOWN)
		equa_num_8 = Tex("8.").scale(0.8).next_to(equa_num_7, 1.6*DOWN)
		equa_num_9 = Tex("9.").scale(0.8).next_to(equa_num_8, 1.6*DOWN)
		equa_num = VGroup(
			equa_num_1,
			equa_num_2,
			equa_num_3,
			equa_num_4,
			equa_num_5,
			equa_num_6,
			equa_num_7,
			equa_num_8,
			equa_num_9,
			)

		equa1 = Tex("A limit can either have one limit value or none.").scale(0.6)
		equa1.next_to(equa_num_1, RIGHT)

		equa2 = MathTex(r"\lim_{n \to \infty }c = c").scale(0.7)
		equa2.next_to(equa_num_2, RIGHT)

		equa3 = MathTex(r"\lim_{n \to \infty }c\cdot a = c\lim_{n \to \infty }a = c\cdot A").scale(0.6)
		equa3.next_to(equa_num_3, RIGHT)

		equa4 = MathTex(r"\lim_{n \to \infty }(a\pm b) = \lim_{n \to \infty }a\pm \lim_{n \to \infty }b = A\pm B").scale(0.6)
		equa4.next_to(equa_num_4, RIGHT)

		equa5 = MathTex(r"\lim_{n \to \infty }(a_{n}\cdot b_{n}) = \lim_{n \to \infty }a_{n}\cdot \lim_{n \to \infty }b_{n} = A\cdot B").scale(0.6)
		equa5.next_to(equa_num_5, RIGHT)

		equa6 = MathTex(r"\lim_{n\to\infty }\frac{a_{n}}{b_{n}}=\frac{\lim_{a\to\infty}a_{n}}{\lim_{a\to\infty}b_{n}}=\frac{A}{B},B\neq 0").scale(0.6)
		equa6.next_to(equa_num_6, RIGHT)

		equa7 = MathTex(r"\lim_{n \to \infty }a_{n}^{k} = ( \lim_{n \to \infty }a_{n} )^{k} = A^{k}").scale(0.6)
		equa7.next_to(equa_num_7, RIGHT)

		equa8 = MathTex(r"\lim_{n\to\infty }\sqrt{a_{n}}=\sqrt{\lim_{n\to\infty }a_{n}}=\sqrt{A}").scale(0.6)
		equa8.next_to(equa_num_8, RIGHT)

		equa9 = MathTex(r"\lim_{n \to \infty }\left | a_{n} \right | = \left |\lim_{n \to \infty }a_{n}  \right | = \left | A \right |").scale(0.6)
		equa9.next_to(equa_num_9, RIGHT)

		equa_group = VGroup(equa1,equa2,equa3,equa4,equa5,equa6,equa7,equa8,equa9)


		equa_head = Tex("Some theories of limit", color = BLUE).scale(1).shift(3.4*UP+3.7*LEFT)

		equa_rect = Line([-15,2.8,0],[15,2.8,0], color=WHITE)

		self.add(equa_head, equa_rect)

		self.play(FadeIn(equa_num))
		
		for i in range(0,9):
			print(i)
			self.play(FadeIn(equa_group[i]))

		self.wait(2)
		
		self.play(equa_group[0].animate.set_color(PINK))
		self.wait()
		self.play(equa_group[0].animate.set_color(WHITE),equa_group[1].animate.set_color(PINK))
		self.wait()
		self.play(equa_group[1].animate.set_color(WHITE),equa_group[2].animate.set_color(PINK))
		self.wait()
		self.play(equa_group[2].animate.set_color(WHITE),equa_group[3].animate.set_color(PINK))
		self.wait()
		self.play(equa_group[3].animate.set_color(WHITE),equa_group[4].animate.set_color(PINK))
		self.wait()
		self.play(equa_group[4].animate.set_color(WHITE),equa_group[5].animate.set_color(PINK))
		self.wait()
		self.play(equa_group[5].animate.set_color(WHITE),equa_group[6].animate.set_color(PINK))
		self.wait()
		self.play(equa_group[6].animate.set_color(WHITE),equa_group[7].animate.set_color(PINK))
		self.wait()
		self.play(equa_group[7].animate.set_color(WHITE),equa_group[8].animate.set_color(PINK))
		self.wait()
		self.play(equa_group[8].animate.set_color(WHITE))

		self.wait(4)
		self.clear()

	def property_ex(self):
		self.camera.background_color = GRAY_E

		screen_rect = Rectangle(width = 8, height=5.5, fill_opacity = 1, fill_color=BLACK)
		simple_ex = Text("Example").scale(0.9).to_edge(UP)

		s_ex_1_0 = Tex("If ").scale(0.7)
		s_ex_1_1 = MathTex(r"\lim_{n \to \infty }a_{n} = 10").scale(0.7).next_to(s_ex_1_0,0.5*RIGHT)
		s_ex_1_2 = Tex(" then what is ").scale(0.8).next_to(s_ex_1_1,0.5*RIGHT)
		s_ex_1_3 = MathTex(r"\lim_{n \to \infty }6\cdot a_{n}").scale(0.7).next_to(s_ex_1_2,0.5*RIGHT)

		s_ex_1 = VGroup(s_ex_1_0,s_ex_1_1,s_ex_1_2,s_ex_1_3).shift(2.1*UP+3*LEFT).set_color(GREEN)


		s_ex_1_sol_0 = MathTex(r"\lim_{n \to \infty }6\cdot a_{n}").scale(0.8).shift(UP)
		s_ex_1_sol_1 = MathTex(r"6\cdot\lim_{n \to \infty }a_{n}").scale(0.8).next_to(s_ex_1_sol_0, DOWN)
		s_ex_1_sol_2 = MathTex(r"6(10)").scale(0.8).next_to(s_ex_1_sol_1, DOWN)
		s_ex_1_sol_3 = MathTex(r"=60").scale(0.8).next_to(s_ex_1_sol_2, DOWN)

		s_ex_1_sol = VGroup(s_ex_1_sol_0, s_ex_1_sol_1, s_ex_1_sol_2, s_ex_1_sol_3)

		self.play(GrowFromCenter(screen_rect))
		self.play(FadeIn(simple_ex))
		self.play(FadeIn(s_ex_1))
		self.wait(2)
		self.play(Write(s_ex_1_sol_0))
		self.wait()
		self.play(TransformFromCopy(s_ex_1_sol_0,s_ex_1_sol_1))
		self.wait()
		self.play(TransformFromCopy(s_ex_1_sol_1,s_ex_1_sol_2))
		self.wait()
		self.play(TransformFromCopy(s_ex_1_sol_2,s_ex_1_sol_3))

		
		self.wait(2)

		self.play(FadeOut(s_ex_1), FadeOut(s_ex_1_sol))

		s_ex_2_0 = Tex("If ").scale(0.7)
		s_ex_2_1 = MathTex(r"\lim_{n\to\infty }a_{n} = 3").scale(0.7).next_to(s_ex_2_0,0.5*RIGHT)
		s_ex_2_2 = Tex(" and ").scale(0.8).next_to(s_ex_2_1,0.5*RIGHT)
		s_ex_2_3 = MathTex(r"\lim_{n\to\infty }b_{n} = 5").scale(0.7).next_to(s_ex_2_2,0.5*RIGHT)
		s_ex_2_4 = Tex(" then what is ").scale(0.7).next_to(s_ex_2_3,0.5*RIGHT)
		s_ex_2_5 = MathTex(r"\lim_{n\to\infty }(a_{n} + b_{n})").scale(0.7).next_to(s_ex_2_1,DOWN)

		s_ex_2 = VGroup(
			s_ex_2_0,
			s_ex_2_1,
			s_ex_2_2,
			s_ex_2_3,
			s_ex_2_4,
			s_ex_2_5
			).shift(2.1*UP+3.2*LEFT).set_color(GREEN)


		s_ex_2_sol_0 = MathTex(r"\lim_{n\to\infty }(a_{n} + b_{n})").scale(0.8).shift(0.5*UP)
		s_ex_2_sol_1 = MathTex(r"\lim_{n\to\infty }a_{n} + \lim_{n\to\infty }b_{n}").scale(0.8).next_to(s_ex_2_sol_0, DOWN)
		s_ex_2_sol_2 = MathTex(r"3+5").scale(0.8).next_to(s_ex_2_sol_1, DOWN)
		s_ex_2_sol_3 = MathTex(r"=8").scale(0.8).next_to(s_ex_2_sol_2, DOWN)

		s_ex_2_sol = VGroup(s_ex_2_sol_0, s_ex_2_sol_1, s_ex_2_sol_2, s_ex_2_sol_3)

		self.play(FadeIn(s_ex_2))
		self.wait(2)
		self.play(Write(s_ex_2_sol_0))
		self.wait()
		self.play(TransformFromCopy(s_ex_2_sol_0,s_ex_2_sol_1))
		self.wait()
		self.play(TransformFromCopy(s_ex_2_sol_1,s_ex_2_sol_2))
		self.wait()
		self.play(TransformFromCopy(s_ex_2_sol_2,s_ex_2_sol_3))
		self.wait(2)

		self.clear()

	def property_extra(self):
		self.camera.background_color = BLACK

		equa_head = Tex("Some theories of limit", color = BLUE).scale(1).shift(3.4*UP+3.7*LEFT)

		equa_rect = Line([-15,2.8,0],[15,2.8,0], color=WHITE)

		equa_num_1 = Tex("1.").shift(5.5*LEFT+2.2*UP).scale(0.8)
		equa_num_2 = Tex("2.").scale(0.8).next_to(equa_num_1, 1.6*DOWN)
		equa_num_3 = Tex("3.").scale(0.8).next_to(equa_num_2, 1.6*DOWN)
		equa_num_4 = Tex("4.").scale(0.8).next_to(equa_num_3, 1.6*DOWN)
		equa_num_5 = Tex("5.").scale(0.8).next_to(equa_num_4, 1.6*DOWN)
		equa_num_6 = Tex("6.").scale(0.8).next_to(equa_num_5, 1.6*DOWN)
		equa_num_7 = Tex("7.").scale(0.8).next_to(equa_num_6, 1.6*DOWN)
		equa_num_8 = Tex("8.").scale(0.8).next_to(equa_num_7, 1.6*DOWN)
		equa_num_9 = Tex("9.").scale(0.8).next_to(equa_num_8, 1.6*DOWN)
		equa_num = VGroup(
			equa_num_1,
			equa_num_2,
			equa_num_3,
			equa_num_4,
			equa_num_5,
			equa_num_6,
			equa_num_7,
			equa_num_8,
			equa_num_9,
			)

		equa1 = Tex("A limit can either have one limit value or none.").scale(0.7)
		equa1.next_to(equa_num_1, RIGHT)

		equa2 = MathTex(r"\lim_{n \to \infty }c = c").scale(0.7)
		equa2.next_to(equa_num_2, RIGHT)

		equa3 = MathTex(r"\lim_{n \to \infty }c\cdot a = c\lim_{n \to \infty }a = c\cdot A").scale(0.6)
		equa3.next_to(equa_num_3, RIGHT)

		equa4 = MathTex(r"\lim_{n \to \infty }(a\pm b) = \lim_{n \to \infty }a\pm \lim_{n \to \infty }b = A\pm B").scale(0.6)
		equa4.next_to(equa_num_4, RIGHT)

		equa5 = MathTex(r"\lim_{n \to \infty }(a_{n}\cdot b_{n}) = \lim_{n \to \infty }a_{n}\cdot \lim_{n \to \infty }b_{n} = A\cdot B").scale(0.6)
		equa5.next_to(equa_num_5, RIGHT)

		equa6 = MathTex(r"\lim_{n\to\infty }\frac{a_{n}}{b_{n}}=\frac{\lim_{a\to\infty}a_{n}}{\lim_{a\to\infty}b_{n}}=\frac{A}{B},B\neq 0").scale(0.6)
		equa6.next_to(equa_num_6, RIGHT)

		equa7 = MathTex(r"\lim_{n \to \infty }a_{n}^{k} = ( \lim_{n \to \infty }a_{n} )^{k} = A^{k}").scale(0.6)
		equa7.next_to(equa_num_7, RIGHT)

		equa8 = MathTex(r"\lim_{n\to\infty }\sqrt{a_{n}}=\sqrt{\lim_{n\to\infty }a_{n}}=\sqrt{A}").scale(0.6)
		equa8.next_to(equa_num_8, RIGHT)

		equa9 = MathTex(r"\lim_{n \to \infty }\left | a_{n} \right | = \left |\lim_{n \to \infty }a_{n}  \right | = \left | A \right |").scale(0.6)
		equa9.next_to(equa_num_9, RIGHT)

		equa_group = VGroup(equa1,equa2,equa3,equa4,equa5,equa6,equa7,equa8,equa9)


		equa_head = Tex("Some theories of limit", color = BLUE).scale(1).shift(3.4*UP+3.7*LEFT)

		equa_rect = Line([-15,2.8,0],[15,2.8,0], color=WHITE)

		self.add(equa_head, equa_rect)

		self.play(FadeIn(equa_num))

		self.add(equa_head, equa_rect, equa_num ,equa_group)
		self.wait()
		self.play(AnimationGroup(
			FadeOut(equa_num, shift=10*LEFT),
			FadeOut(equa_group, shift=10*LEFT),
			)
		)

		equa_num_10 = Tex("10.").shift(5.5*LEFT+2*UP)

		equa_num_10_sub_1 = Tex("1)").next_to(equa_num_10, RIGHT)
		equa_num_10_sub_2 = Tex("2)").next_to(equa_num_10_sub_1, DOWN)

		equa10_sub_1 = MathTex(r"\lim_{n \to \infty }n^{k} = \infty ; k \in +\mathbb{R}").scale(0.8)
		equa10_sub_1.next_to(equa_num_10_sub_1, RIGHT)

		equa10_sub_2 = MathTex(r"\lim_{n \to \infty }\frac{c}{n^{k}}=0").scale(0.8)
		equa10_sub_2.next_to(equa_num_10_sub_2, RIGHT)

		equa10_rect = SurroundingRectangle(equa10_sub_1, color = WHITE)

		self.play(FadeIn(equa_num_10, shift=3*LEFT))
		self.play(FadeIn(equa_num_10_sub_1, shift=3*LEFT))
		self.play(FadeIn(equa10_sub_1, shift=3*LEFT))

		self.wait(3)

		#self.play(Create(equa10_rect))

		equa10_sub_1.save_state()
		equa_num_10.save_state()
		equa_head.save_state()
		equa_rect.save_state()
		equa_num_10_sub_1.save_state()

		self.clear()

		self.expovalue_1()

		self.play(
			Restore(equa10_sub_1),
			Restore(equa_num_10_sub_1),
			Restore(equa_num_10),
			Restore(equa_head),
			Restore(equa_rect)
			)

		self.wait()

		self.play(FadeIn(equa_num_10_sub_2))
		self.play(FadeIn(equa10_sub_2))

		self.wait(3)
		self.clear()


	def expovalue_1(self):

		self.color = itertools.cycle(self.EXPO_COLOR)
		NEW_COLOR = [RED,ORANGE,GOLD,YELLOW,GREEN,TEAL,BLUE,PURPLE,PINK,LIGHT_PINK]

		p = ValueTracker(1)

		expo_ax = Axes(
			x_range = [-1,5,1],
			x_length = 18,
			y_range = [-1,7,1], 
			y_length = 8, 
			tips = False
			)
		self.play(Create(expo_ax))

		for i in range(1,10):
			expo = expo_ax.get_graph(lambda x: x**i ,color = BLUE, x_range=[0.2,3]).set_color(next(self.color))
			expo_group = VGroup(*[expo])

			k_base = Tex("n").shift(2*RIGHT,2*DOWN).set_color(NEW_COLOR[i-1])
			k = DecimalNumber(1, num_decimal_places = 0).set_color(NEW_COLOR[i-1])
			k.add_updater(lambda d: d.set_value(i)).next_to(k_base,0.3*UP+0.3*RIGHT)
			k_group = VGroup(k_base, k)
			#k_rect = SurroundingRectangle(k, color = WHITE, stroke_width = 0.5)

			self.play(FadeIn(expo), FadeIn(k), FadeIn(k_base)) #FadeIn(k_rect))
		
		self.wait(2)

		expo_num = DecimalNumber(1, num_decimal_places=0).shift(3.5*RIGHT)
		expo_num.add_updater(lambda m: m.set_value(p.get_value()))

		expo_re = expo_ax.get_graph(lambda x: x**p.get_value(), color = WHITE, x_range=[0.2,3])
		expo_re.add_updater(
			lambda m: m.become(
				expo_ax.get_graph(
					lambda x: x**p.get_value(), 
					color = WHITE, 
					x_range=[0.2,3],
					)
				)
			)
		self.play(Create(expo_re))#,Create(expo_num))
		#self.play(
			#ApplyMethod(p.increment_value,9),
            #run_time = 5,
			#)
		
		expo_div_1 = MathTex(r"n^{k} ; k \in +\mathbb{R}").shift(2*RIGHT,2.4*UP)
		expo_div_2 = Tex("is Divergent").next_to(expo_div_1,0.5*RIGHT)
		expo_div = VGroup(expo_div_1, expo_div_2).add_background_rectangle()
		
		self.play(FadeIn(expo_div), AnimationGroup(
			ApplyMethod(p.increment_value,9),
            run_time = 5,
			)
		)

		self.wait(3)

		self.clear()

	def there_are_4_ways(self):
		self.camera.background_color = GRAY_E

		brace_limit = Tex("-")
		brace_group = VGroup(*[brace_limit.copy() for i in range(4)])
		brace_group.arrange(4*DOWN)
		brace_group.to_edge(RIGHT, buff = 4.7)
		
		limit_1 = Tex("polynomial").next_to(brace_group[0], 0.3*RIGHT).scale(0.9)
		limit_2 = Tex("polynomial fractions").next_to(brace_group[1], 0.3*RIGHT).scale(0.9)
		limit_3 = Tex("Exponential").next_to(brace_group[2], 0.3*RIGHT).scale(0.9)
		limit_4 = Tex("squre root").next_to(brace_group[3], 0.3*RIGHT).scale(0.9)
		limit = VGroup(limit_1, limit_2, limit_3, limit_4)

		limit_1_rect = SurroundingRectangle(limit_1, color = RED)
		limit_2_rect = SurroundingRectangle(limit_2, color = ORANGE)
		limit_3_rect = SurroundingRectangle(limit_3, color = YELLOW_E)
		limit_4_rect = SurroundingRectangle(limit_4, color = GREEN)

		limit_rect_stroke = Rectangle(
			width = 7, 
			height= 6,  
			fill_opacity =0,
		).shift(1.7*LEFT)

		limit_rect_bg = Rectangle(
			width = 7, 
			height= 6, 
			fill_color = BLACK, 
			fill_opacity =1,
			stroke_opacity = 0,
		).shift(1.7*LEFT)

		limit_rect = VGroup(limit_rect_bg, limit_rect_stroke)

		limit_1_ex = MathTex(r"a_{n} = 5n^4+2n^3-6n+3").shift(2*LEFT).scale(0.7)
		limit_2_ex = MathTex(r"a_{n} = \frac{3n+4}{n+1}").shift(2*LEFT).scale(0.7)
		limit_3_ex = MathTex(r"a_{n} = \frac{1}{3^{(2-n)}}").shift(2*LEFT).scale(0.7)
		limit_4_ex = MathTex(r"a_{n} = \sqrt{\frac{1}{9}n^{4}-18n^{2}+9}").shift(2*LEFT).scale(0.7)

		self.play(DrawBorderThenFill(limit_rect))


		self.play(FadeIn(brace_group),FadeIn(limit))
		self.wait()

		self.play(AnimationGroup(Create(limit_1_rect), FadeIn(limit_1_ex), limit_rect_stroke.animate.set_color(RED)))

		#self.add(limit_1_rect, limit_rect_stroke.set_color(RED) ,limit_1_ex)

		self.wait(2)

		self.add_sound("clack")
		self.remove(limit_1_rect, limit_1_ex)
		self.add(limit_2_rect, limit_rect_stroke.set_color(ORANGE) ,limit_2_ex)

		self.wait(2)

		self.add_sound("clack")
		self.remove(limit_2_rect, limit_2_ex)
		self.add(limit_3_rect, limit_rect_stroke.set_color(YELLOW_E) ,limit_3_ex)

		self.wait(2)

		self.add_sound("clack")
		self.remove(limit_3_rect, limit_3_ex)
		self.add(limit_4_rect, limit_rect_stroke.set_color(GREEN) ,limit_4_ex)


		self.wait(2)

		self.clear()

class Section4(Scene):

	def construct(self):
		#self.intro_infinite()
		#self.depend_on_series()
		#self.infinite_sum()
		#self.infinite_sum_formula()
		#self.for_reminder()
		#self.infinite_1()
		#self.Geometric_formula()
		self.conclusion_infinit()
		#self.example_infinite()
		self.wait(5)
		#self.ex_next()
		#self.Harmonic()

	def intro_infinite(self):
		bubble = SVGMobject("Bubbles_thought", color = WHITE, fill_opacity = 0).scale(4.5).shift(DOWN)
		another_ways = Text("what about infinite sum?").scale(0.7)
		self.play(FadeIn(bubble))
		self.play(FadeIn(another_ways))
		self.wait(2)
		self.clear()

	def depend_on_series(self):
		cover_rect = Rectangle(width=15, height = 15 ,fill_color = BLACK,fill_opacity=1)
		self.add(cover_rect)

		depend = Tex("Convergent"," or ","Divergent")
		self.play(FadeIn(depend))
		self.wait()
		self.play(Wiggle(depend[0], n_wiggles=3), run_time = 2)
		self.play(Wiggle(depend[2], n_wiggles=3), run_time = 2)
		self.wait(2)

		self.remove(depend, cover_rect)


	def infinite_sum(self):
		#self.color = itertools.cycle(self.NUM_LINE_COLOR)
		
		infinite_s1 = MathTex(r"\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\frac{1}{16}")
		tri_dot = Tex("...")
		equal1 = MathTex(r"=1")

		def update_up(mob):
			mob.next_to(infinite_s1, RIGHT)

		def upadate_up2(mob):
			mob.next_to(tri_dot,RIGHT)

		nl = NumberLine(
			x_range=[0,1,0.25],
			numbers_with_elongated_ticks=[0,1],
			length=10,color=BLUE,
			decimal_number_config={"num_decimal_places": 0},
			include_numbers = True,
			numbers_to_include = [0,1],
			).shift(1.8*DOWN)
		
		sum_brace1 = BraceBetweenPoints(nl.n2p(0),nl.n2p(0.5),UP)
		sum_line1 = Line(nl.n2p(0),nl.n2p(0.5)).set_color(RED_A)
		sum_tex1 = MathTex(r"\frac{1}{2}").next_to(sum_brace1,0.7*UP).set_color(RED_A).scale(0.7)
		sum_1 = VGroup(sum_brace1, sum_line1)

		sum_brace2 = BraceBetweenPoints(nl.n2p(0.5),nl.n2p(0.75),UP)
		sum_line2 = Line(nl.n2p(0.5),nl.n2p(0.75)).set_color(RED)
		sum_tex2 = MathTex(r"\frac{1}{4}").next_to(sum_brace2,0.7*UP).set_color(RED).scale(0.7)
		sum_2 = VGroup(sum_brace2, sum_line2)

		sum_brace3 = BraceBetweenPoints(nl.n2p(0.75),nl.n2p(0.875),UP)
		sum_line3 = Line(nl.n2p(0.75),nl.n2p(0.875)).set_color(RED_A)
		sum_tex3 = MathTex(r"\frac{1}{8}").next_to(sum_brace3,0.7*UP).set_color(RED_A).scale(0.7)
		sum_3 = VGroup(sum_brace3, sum_line3)

		sum_brace4 = BraceBetweenPoints(nl.n2p(0.875),nl.n2p(0.9375),UP)
		sum_line4 = Line(nl.n2p(0.875),nl.n2p(0.9375)).set_color(RED)
		sum_tex4 = MathTex(r"\frac{1}{16}").next_to(sum_brace4,0.7*UP).set_color(RED).scale(0.7)
		sum_4 = VGroup(sum_brace4, sum_line4)

		sum_brace5 = BraceBetweenPoints(nl.n2p(0.9375),nl.n2p(0.96875),UP)
		sum_line5 = Line(nl.n2p(0.9375),nl.n2p(0.96875)).set_color(RED_A)
		#sum_tex5 = MathTex(r"\frac{1}{16}").next_to(sum_brace5,UP).set_color(RED_A)
		sum_5 = VGroup(sum_brace5, sum_line5)

		sum_brace6 = BraceBetweenPoints(nl.n2p(0.96875),nl.n2p(0.984375),UP)
		sum_line6 = Line(nl.n2p(0.96875),nl.n2p(0.984375)).set_color(RED)
		#sum_tex6 = MathTex(r"\frac{1}{64}").next_to(sum_brace6,UP).set_color(RED)
		sum_6 = VGroup(sum_brace6, sum_line6)

		sum_brace7 = BraceBetweenPoints(nl.n2p(0.984375),nl.n2p(0.99921875),UP)
		sum_line7 = Line(nl.n2p(0.984375),nl.n2p(0.99921875)).set_color(RED_A)
		sum_7 = VGroup(sum_brace7, sum_line7)
		#sum_tex7 = MathTex(r"\frac_{1}{64}").next_to(sum_brace6,UP).set_color(RED)

		triple_dot = Tex('...').next_to(sum_tex4,RIGHT)

		sum_brace = VGroup(
			sum_brace1, 
			sum_brace2, 
			sum_brace3, 
			sum_brace4,
			sum_brace5,
			sum_brace6, 
			sum_line1, 
			sum_line2, 
			sum_line3, 
			sum_line4,
			sum_line5,
			sum_line6,
			sum_line7,
			sum_tex1,
			sum_tex2,
			sum_tex3,
			sum_tex4,
			)
		
		self.play(FadeIn(infinite_s1))
		self.wait()
		tri_dot.add_updater(update_up)
		self.play(FadeIn(tri_dot))
		self.wait()
		self.play(infinite_s1.animate.to_edge(UP))


		self.play(Write(nl))
		self.wait()

		self.play(AnimationGroup(
			GrowFromEdge(sum_line1, LEFT),
			GrowFromEdge(sum_brace1,LEFT),
			FadeIn(sum_tex1),
			lag_ratio = 0.5,
			)
		)
		self.play(AnimationGroup(
			GrowFromEdge(sum_line2, LEFT),
			GrowFromEdge(sum_brace2,LEFT),
			FadeIn(sum_tex2),
			lag_ratio = 0.5,
			)
		)
		self.play(AnimationGroup(
			GrowFromEdge(sum_line3, LEFT),
			GrowFromEdge(sum_brace3,LEFT),
			FadeIn(sum_tex3),
			lag_ratio = 0.5,
			)
		)
		self.play(AnimationGroup(
			GrowFromEdge(sum_line4, LEFT),
			GrowFromEdge(sum_brace4,LEFT),
			FadeIn(sum_tex4),
			lag_ratio = 0.5,
			)
		)
		self.play(AnimationGroup(
			GrowFromEdge(sum_line5, LEFT),
			GrowFromEdge(sum_brace5,LEFT),
			lag_ratio = 0.5,
			)
		)
		self.play(AnimationGroup(
			GrowFromEdge(sum_line6, LEFT),
			GrowFromEdge(sum_brace6,LEFT),
			lag_ratio = 0.5,
			)
		)
		self.play(AnimationGroup(
			GrowFromEdge(sum_line7, LEFT),
			lag_ratio = 0.5,
			)
		)
		self.play(FadeIn(triple_dot))

		#self.play(GrowFromEdge(sum_line1, LEFT))
		#self.play(GrowFromEdge(sum_brace1, LEFT))
		self.wait()

		conv_tex = Tex("converge to 1").shift(2.5*DOWN).set_color(RED)

		self.play(Write(conv_tex))
		equal1.add_updater(upadate_up2)
		self.play(FadeIn(equal1))
		self.wait(3)

	def Harmonic(self):
		pass 

	def infinite_sum_formula(self):
		
		infinite_sigma = MathTex(r"S_{\infty }=\sum_{n=1}^{\infty }a_{n}",r"=",r"\lim_{n\to\infty }",r"S_{n}").scale(0.8).shift(1.2*UP)
		rect_indicate = SurroundingRectangle(infinite_sigma, color = RED_A)
		#arrow_limit = Arrow([1.1,-0.15,0],[1.1,-1.5,0], color = YELLOW)
		#limit_text = Text("infinite sum", color = YELLOW).scale(0.5).next_to(arrow_limit, 0.5*DOWN)

		self.play(AnimationGroup(
			Write(infinite_sigma)
			)
		)
		self.play(Write(rect_indicate))
		#self.play(GrowArrow(arrow_limit))
		#self.play(FadeIn(limit_text))

		self.wait(3)

		self.clear()

	def for_reminder(self):
		speech = SVGMobject("Bubbles_speech",color = WHITE ,fill_opacity =0).scale(3.5)
		talk = Tex("Just For Reminder ...").scale(1.5).shift(UP)
		self.play(Create(speech))
		self.play(FadeIn(talk))
		self.wait(3)
		self.clear()


	def infinite_1(self):
		self.camera.background_color = GRAY_E
		
		b_rect = Rectangle(height=5, width=8, fill_opacity=1,fill_color=BLACK).shift(0.5*DOWN)

		formula = Tex("Formula for Arithmetic Series", color = BLUE).next_to(b_rect,1.5*UP)

		a_s_f = Tex("1.").scale(0.8).shift(UP,2*LEFT)
		formula_a = MathTex(r"S_{n} = \frac{n}{2}(a_{1}+a_{n})").scale(0.8).next_to(a_s_f, RIGHT)

		g_s_f = Tex("2.").scale(0.8).shift(DOWN, 2*LEFT)
		formula_g = MathTex(r"S_{n} = \frac{n}{2}(2a_{1}+(n-1)d)").scale(0.8).next_to(g_s_f, RIGHT)

		self.add(b_rect)
		self.play(FadeIn(formula))
		self.play(AnimationGroup(
			FadeIn(a_s_f),
			FadeIn(formula_a),
			lag_ratio =1,
			)
		)
		self.wait()
		self.play(AnimationGroup(
			FadeIn(g_s_f),
			FadeIn(formula_g),
			lag_ratio =1,
			)
		)
		self.wait(3)
		self.clear()

	def Geometric_formula(self):
		self.camera.background_color = GRAY_E
		g_rect = Rectangle(height=5, width=8, fill_opacity=1,fill_color=BLACK).shift(0.5*DOWN)

		formula = Tex("Formula for Geometric Series", color = BLUE).next_to(g_rect,1.5*UP)

		g_formula = Tex("When r > 1",color = YELLOW).scale(0.8).shift(UP,1.5*LEFT)
		g_f_1 = MathTex(r"S_{n}=a_{1}(\frac{r^{n}-1}{r-1})").scale(0.8).next_to(g_formula, DOWN)
		g_g_1 = VGroup(g_formula, g_f_1)
		rect_g_1 = SurroundingRectangle(g_g_1, color = WHITE)

		g_1_formula = Tex("When r < 1", color = YELLOW).scale(0.8).shift(DOWN, 1.5*LEFT)
		g_f_2 = MathTex(r"S_{n}=a_{1}(\frac{1-r^{n}}{1-r})").scale(0.8).next_to(g_1_formula, DOWN)
		g_g_2 = VGroup(g_1_formula, g_f_2)
		rect_g_2 = SurroundingRectangle(g_g_2, color = WHITE)

		g_f_3 = MathTex(r"S_{n}=\frac{a_{n}r-a_{1}}{r-1}").scale(0.8).shift(1.7*RIGHT,0.5*DOWN)
		rect_g_f_3 = SurroundingRectangle(g_f_3)
		

		self.add(g_rect)
		self.play(FadeIn(formula))
		self.play(AnimationGroup(
			FadeIn(g_formula),
			FadeIn(g_f_1),
			Create(rect_g_1),
			lag_ratio =1,
			)
		)
		self.wait()
		self.play(AnimationGroup(
			FadeIn(g_1_formula),
			FadeIn(g_f_2),
			Create(rect_g_2),
			lag_ratio =1,
			)
		)
		self.wait()
		self.play(FadeIn(g_f_3))
		self.play(Create(rect_g_f_3))
		self.wait(3)
		self.clear()

	def conclusion_infinit(self):
		self.camera.background_color = BLACK

		geo = Tex("Geometric Series Conclusion").to_edge(UP).set_color(BLUE)
		con_dot_1 = Dot([-4.5,1.5,0])
		con_dot_2 = Dot([-4.5,-1.5,0])
		con_1_1 = Tex("When").next_to(con_dot_1, 0.7*RIGHT)
		con_1_2 = MathTex(r"\left | r \right |<1").next_to(con_1_1, 0.5*RIGHT)
		con_1_3 = Tex(",the sum of the series will be convergent").next_to(con_1_2, 0.5*RIGHT)
		con_1 = VGroup(con_1_1, con_1_2, con_1_3).scale(0.8)

		con_2_1 = Tex("When").next_to(con_dot_2, 0.7*RIGHT)
		con_2_2 = MathTex(r"\left | r \right |\geq 1").next_to(con_2_1, 0.5*RIGHT)
		con_2_3 = Tex(",the sum of the series will be divergent").next_to(con_2_2, 0.5*RIGHT)
		con_2 = VGroup(con_2_1, con_2_2, con_2_3).scale(0.8)

		self.play(FadeIn(geo))
		self.play(GrowFromCenter(con_dot_1))
		self.play(FadeIn(con_1))
		self.wait()
		self.play(GrowFromCenter(con_dot_2))
		self.play(FadeIn(con_2))
		self.wait(2)
		self.clear()

	def example_infinite(self):

						  #0    1    2    3    4     5    6      7
		series = MathTex(r"3",r"+",r"9",r"+",r"27",r"+",r"81",r"+...").scale(1.5).shift(1.9*LEFT,1.5*UP)
		series_idicate_g = VGroup(*[series[i] for i in range(0,7,2)])

		def indicate_g(mob):
			mob.set_color(YELLOW)
			return mob 

		speech = SVGMobject("speech_edge").scale(1.5).to_edge(UR)
		speech_tex = MathTex(r"\left | r \right |\geq 1").shift(2.1*UP,4.1*RIGHT)
		speech_tex_new = MathTex(r"\left | r \right |<1").shift(2.1*UP,4.1*RIGHT)

		arrow = Arrow(3*LEFT,3*RIGHT,color=YELLOW).next_to(series,DOWN)
		arrow_tex = Tex("getting bigger",color = YELLOW).next_to(arrow, 0.6*DOWN)
		arrow_obj = VGroup(arrow, arrow_tex)


		LINE_COLOR = [RED_A,RED]
		COLOR = True

		nl = NumberLine(
			x_range=[0,65,1.25],
			length=26,
			numbers_with_elongated_ticks=[0,5,10,15,20,25,30,35,40,45,50,55,60,65],
			include_numbers=True,
			numbers_to_include= [0,5,10,15,20,25,30,35,40,45,50,55,60,65],
			decimal_number_config={"num_decimal_places": 0},
			color = BLUE,
			).shift(2*DOWN)
		nl.to_edge(LEFT,buff=0)

		sum_brace = []
		sum_line=[]
		SUM=[]
		#sum_tex=[]
		a,b=0,3
		for i in range(0,3,1):
			COLOR = int(not(COLOR))
			sum_brace.append(BraceBetweenPoints(nl.n2p(a),nl.n2p(b),UP))
			sum_line.append(Line(nl.n2p(a),nl.n2p(b)).set_color(LINE_COLOR[COLOR]))
			#STR = str(2**(i+1))
			#sum_tex.append(MathTex("\\frac{1}"+STR).next_to(sum_brace[i],UP).set_color(RED_A).scale(0.7))
			SUM.append(VGroup(sum_brace[i],sum_line[i]))
			a=a+3**(i+1)
			b=b+3**(i+2)

		sum_brace_group = Group(*[sum_brace[i] for i in range(3)])
		sum_line_group= Group(*[sum_line[i] for i in range(3)])
		
		sum_tex = Tex("3","9","27")

		sum_tex[0].next_to(sum_brace_group[0],UP)
		sum_tex[1].next_to(sum_brace_group[1],UP)
		sum_tex[2].next_to(sum_brace_group[2],UP)


		#self.add(nl,sum_brace_group,sum_line_group)
		self.play(FadeIn(series))
		self.play(Create(nl))
		for i in range(0,3):
			self.play(AnimationGroup(
				GrowFromEdge(sum_brace_group[i], LEFT),
				GrowFromEdge(sum_line_group[i], LEFT),
				FadeIn(sum_tex[i]),
				lag_ratio = 0.5,
				run_time = 1.5,				)
			)
		self.wait()
		self.play(AnimationGroup(
			GrowArrow(arrow),
			FadeIn(arrow_tex),
			lag_ratio = 1
			)
		)
		self.wait(2)

		self.play(
			FadeIn(speech),
			Write(speech_tex),
			AnimationGroup(*[ApplyFunction(
					indicate_g,
					series_idicate_g,
					rate_func = there_and_back,
					lag_ratio = 1,
					run_time = 5,
					)
				for mob in series_idicate_g
				]
			)
		)

		self.wait(2)

		series_new = MathTex(r"16+12+9+...").scale(1.5).shift(1.9*LEFT,1.5*UP)


		sum_brace_new_1 = BraceBetweenPoints(nl.n2p(0),nl.n2p(16),UP)
		sum_brace_new_2 = BraceBetweenPoints(nl.n2p(16),nl.n2p(28),UP)
		sum_brace_new_3 = BraceBetweenPoints(nl.n2p(28),nl.n2p(37),UP)
		sum_brace_new_4 = BraceBetweenPoints(nl.n2p(37),nl.n2p(43.75),UP)
		sum_brace_new_5 = BraceBetweenPoints(nl.n2p(43.75),nl.n2p(48.8125),UP)
		sum_brace_new_6 = BraceBetweenPoints(nl.n2p(48.8125),nl.n2p(52.60937),UP)
		sum_brace_new_7 = BraceBetweenPoints(nl.n2p(52.60937),nl.n2p(55.45697),UP)
		sum_brace_new_8 = BraceBetweenPoints(nl.n2p(55.45697),nl.n2p(57.59267), UP)
		sum_brace_new_9 = BraceBetweenPoints(nl.n2p(57.59267),nl.n2p(59.19444), UP)
		sum_brace_new_10 = BraceBetweenPoints(nl.n2p(59.19444),nl.n2p(60.39577), UP)
		sum_brace_new_11 = BraceBetweenPoints(nl.n2p(60.39577),nl.n2p(61.29577), UP)

		tri_dot_new = Tex("...").scale(0.9).next_to(sum_brace_new_11,0.5*RIGHT)


		sum_brace_new = VGroup(
			sum_brace_new_1, 
			sum_brace_new_2, 
			sum_brace_new_3, 
			sum_brace_new_4, 
			sum_brace_new_5, 
			sum_brace_new_6, 
			sum_brace_new_7, 
			sum_brace_new_8, 
			sum_brace_new_9, 
			sum_brace_new_9, 
			sum_brace_new_10, 
			sum_brace_new_11,
			tri_dot_new,
			)

		sum_line_new_1 = Line(nl.n2p(0),nl.n2p(16), color = RED_A)
		sum_line_new_2 = Line(nl.n2p(16),nl.n2p(28), color = RED)
		sum_line_new_3 = Line(nl.n2p(28),nl.n2p(37), color = RED_A)
		sum_line_new_4 = Line(nl.n2p(37),nl.n2p(43.75), color = RED)
		sum_line_new_5 = Line(nl.n2p(43.75),nl.n2p(48.8125), color = RED_A)
		sum_line_new_6 = Line(nl.n2p(48.8125),nl.n2p(52.60937), color = RED)
		sum_line_new_7 = Line(nl.n2p(52.60937),nl.n2p(55.45697), color = RED_A)
		sum_line_new_8 = Line(nl.n2p(55.45697),nl.n2p(57.59267), color = RED)
		sum_line_new_9 = Line(nl.n2p(57.59267),nl.n2p(59.19444), color = RED_A)
		sum_line_new_10 = Line(nl.n2p(59.19444),nl.n2p(60.39577), color = RED)
		sum_line_new_11 = Line(nl.n2p(60.39577),nl.n2p(61.29577), color = RED_A)
		sum_line_new_12 = Line(nl.n2p(61.29577),nl.n2p(61.97077), color = RED)
		sum_line_new_13 = Line(nl.n2p(61.97077),nl.n2p(62.47702), color = RED_A)
		sum_line_new_14 = Line(nl.n2p(62.47702),nl.n2p(62.8567), color = RED)

		sum_tex_new = MathTex(r"16",r"12",r"9")
		sum_tex_new[0].next_to(sum_brace_new[0], UP)
		sum_tex_new[1].next_to(sum_brace_new[1], UP)
		sum_tex_new[2].next_to(sum_brace_new[2], UP)

		sum_line_new = VGroup(
			sum_line_new_1, 
			sum_line_new_2, 
			sum_line_new_3, 
			sum_line_new_4, 
			sum_line_new_5, 
			sum_line_new_6, 
			sum_line_new_7,
			sum_line_new_8,
			sum_line_new_9,
			sum_line_new_10,
			sum_line_new_11,
			sum_line_new_12,
			sum_line_new_13,
			sum_line_new_14,
			)

		animate_group = VGroup(nl, sum_line_new, sum_brace_new, sum_tex_new)

		self.play(
			FadeOut(arrow_obj),
			FadeOut(speech),
			FadeOut(speech_tex),
			)
		self.play(ReplacementTransform(series,series_new))
		self.play(
			ReplacementTransform(sum_brace_group, sum_brace_new),
			ReplacementTransform(sum_line_group, sum_line_new), 
			FadeOut(sum_tex), 
			ReplacementTransform(sum_tex,sum_tex_new)),
		conv = Tex("Convergent", color = YELLOW).next_to(series_new, DOWN)
		self.wait()
		self.play(animate_group.animate.shift(15*LEFT), run_time = 2, rate_func = rate_functions.ease_in_out_cubic)
		self.wait()
		self.play(FadeIn(speech),FadeIn(speech_tex_new))
		self.play(Write(conv))
		
		self.wait(3)
		self.play(FadeOut(sum_line_new,sum_brace_new, series_new, speech, speech_tex_new, conv),Uncreate(nl),lag_ratio=0.8)
		self.wait()

class Section5(ZoomedScene):

	def __init__(self, **kwargs):
		ZoomedScene.__init__(
			self,
			zoom_factor=0.3,
			zoomed_display_height=2.3,
			zoomed_display_width=4.5,
			image_frame_stroke_width=20,
			zoomed_camera_config={
				"default_frame_stroke_width": 3,
				},
			**kwargs
		)


	def construct(self):
		self.equal1()		

	def equal1(self):

		zoomed_camera = self.zoomed_camera
		zoomed_display = self.zoomed_display
		frame = zoomed_camera.frame
		zoomed_display_frame = zoomed_display.display_frame

		def update_dot(mob):
			mob.move_to(dot.get_center())

		frame.add_updater(update_dot)

		equa = MathTex(r"\frac{9}{10}",r"+",r"\frac{9}{100}",r"+",r"\frac{9}{1000}",r"+",r"...").to_edge(UP)
		equal_1 = MathTex(r"= 1").next_to(equa,0.5*RIGHT)
		equa2 = MathTex(r"0.999... = 1").scale(2)
		equa_g = VGroup(equa, equal_1)
		equa_num = VGroup(equa[0],equa[2],equa[4])
		nl = NumberLine(x_range=[0,1,0.1],
			numbers_with_elongated_ticks=[0,0.5,1],
			length=10,color=WHITE,
			decimal_number_config={"num_decimal_places": 0},
			include_numbers = True,
			numbers_to_include = [0,1],
			)
		nl.shift(0.5*UP)
		dot = Dot(nl.n2p(0),color=YELLOW,radius=0.02)
		zoomed_display.next_to(nl,DOWN)

		dashed_line = DashedLine(
			nl.n2p(0),
			nl.n2p(1),
			dash_length=0.7,
			dashed_ratio=4,
			color=YELLOW,
			).set_stroke(width=11)
		line0 = Line(nl.n2p(0),nl.n2p(0.9),stroke_width=1.5).set_color(BLUE)
		line1 = Line(nl.n2p(0.9),nl.n2p(0.99),stroke_width=1.5).set_color(BLUE_E)
		line2 = Line(nl.n2p(0.99),nl.n2p(0.999),stroke_width=1.5).set_color(BLUE)

		num = DecimalNumber(0, num_decimal_places=3)

		triangle = RegularPolygon(3,start_angle=-PI/2).scale(0.2)

		def update_tri(mob):
			mob.next_to(dot,0.6*UP)

		def update_num(mob):
			mob.next_to(triangle,UP)

		#def update_num_new(mob):
			#mob.next_to(zoomed_display,RIGHT)

		num.add_updater(update_num)
		triangle.add_updater(update_tri)

		t_label = VGroup(num,triangle)

		self.play(FadeIn(equa))

		self.play(Create(nl))
		self.play(Create(dot))
		self.play(
			LaggedStart(
				*[ShowPassingFlash(dashed_segment)
				for dashed_segment in dashed_line],
				run_time=5
				),
			AnimationGroup(
				Animation(Mobject(), run_time=2.1),
				)
			)

		self.wait()
		self.play(Create(triangle),FadeIn(num))
		self.wait()
		
		self.play(
			dot.animate.move_to(nl.n2p(0.9)),
			GrowFromEdge(line0,LEFT),
			ChangeDecimalToValue(
				decimal_mob=num,
				target_number=0.9
				),
			lag_ratio=0,
			run_time=3,
			rate_func=linear
			)
		self.wait()
		self.play(Indicate(equa[0]))
		self.wait()
		self.play(Create(frame))
		#num.remove_updater(update_num)
		#num.add_updater(update_num_new)
		self.activate_zooming()
		self.play(self.get_zoomed_display_pop_out_animation())
		
		self.play(
			dot.animate.move_to(nl.n2p(0.99)),
			GrowFromEdge(line1,LEFT),
			ChangeDecimalToValue(
				decimal_mob=num,
				target_number=0.99
				),
			lag_ratio=0,
			run_time=2,
			rate_func=linear
			)
		self.wait()
		self.play(Indicate(equa[2]))
		self.wait()

		self.play(
			dot.animate.move_to(nl.n2p(0.999)),
			GrowFromEdge(line2,LEFT),
			ChangeDecimalToValue(
				decimal_mob=num,
				target_number=0.999
				),
			lag_ratio=0,
			run_time=1,
			rate_func=linear
			)
		self.wait()
		self.play(Indicate(equa[4]))
		self.wait()
		self.play(FadeIn(equal_1))
		self.wait()
		self.play(self.get_zoomed_display_pop_out_animation(),rate_func=lambda t: smooth(1 - t))
		self.play(
			Uncreate(zoomed_display_frame), 
			FadeOut(frame), 
			Uncreate(nl), 
			Uncreate(t_label),
			FadeOut(line0),
			FadeOut(line1),
			FadeOut(line2),
			FadeOut(dot),
			lag_ratio = 0,
			)
		self.play(ReplacementTransform(equa_g,equa2))
		self.wait(2)
		self.clear()

class Section5_Ex(MovingCameraScene):
	def construct(self):
		self.square_riddle()

	def square_riddle(self):
		obj_square_1 = Rectangle(width=4, height=4)
		obj_square_2 = Rectangle(width=2*np.sqrt(2), height=2*np.sqrt(2)).rotate(PI/4)
		#square_0 = Rectangle(height=4, width=4)
		#square_1 = Rectangle(height = np.sqrt(8), width = np.sqrt(8)).rotate(PI/4)	
		square_g = VGroup()
		cycle_color = [RED_D, RED_B]*5
		a = 4
		for i in range(0,6,1):
			square = VGroup(*[Rectangle(height=a ,width=a).rotate((PI/4)*i)]).set_color(cycle_color[i])
			a = (a/2)*np.sqrt(2)
			print(a)
			print(square)
			square_g.add(square)
			self.play(Create(square))

		self.wait()

		for i in range(0,6,1):
			self.play(square_g[i].animate.set_color(WHITE),rate_func=there_and_back,lag_ratio=0.1)

		self.play(AnimationGroup(FadeOut(square_g[2]),FadeOut(square_g[3]),FadeOut(square_g[4]),FadeOut(square_g[5]),lag_ratio=0.2))
		self.wait()
		self.camera.frame.save_state()
		self.play(self.camera.frame.animate.move_to(1.2*RIGHT + 1.2*UP).set(width=8))

		p1 = obj_square_1.point_from_proportion(0)
		p2 = obj_square_1.point_from_proportion(0.125)
		p3 = obj_square_1.point_from_proportion(0.875)

		p4 = obj_square_2.point_from_proportion(0)
		p5 = obj_square_2.point_from_proportion(0.75)

		brace1 = BraceBetweenPoints(p1, p2, stroke_width = 0.1)
		b1_tex = MathTex(r"\frac{1}{2}").shift(RIGHT,2.85*UP).scale(0.5)
		brace2 = BraceBetweenPoints(p3, p1, stroke_width = 0.1)
		b2_tex = MathTex(r"\frac{1}{2}").next_to(brace2, RIGHT, buff = 0.1).scale(0.5)
		brace3 = BraceBetweenPoints(p4, p5, stroke_width = 0.1, color=BLUE_C)
		b3_tex = MathTex(r"\frac{\sqrt{2}}{2}",color=BLUE_C).shift(0.4*UP,0.4*RIGHT).scale(0.5)
		self.play(GrowFromEdge(brace1, LEFT), GrowFromEdge(brace2, DOWN))
		self.play(FadeIn(b1_tex),FadeIn(b2_tex))
		self.wait()
		self.play(GrowFromEdge(brace3, LEFT+UP))
		self.play(FadeIn(b3_tex))

		group = VGroup(brace1, brace2, brace3, b1_tex, b2_tex, b3_tex)

		self.wait()
		self.play(Restore(self.camera.frame))
		self.play(FadeOut(group))
		self.wait()
		self.play(AnimationGroup(Create(square_g[2]),Create(square_g[3]),Create(square_g[4]),Create(square_g[5]),lag_ratio=0.4))
		self.play(square_g.animate.shift(2.6*LEFT))
		self.wait()

		dot1 = Dot().shift(1.5*UP)
		dot2 = Dot().shift(0.5*UP)
		dot3 = Dot().shift(0.5*DOWN)

		solution = MathTex(r"S_{\infty }=(4\cdot 1)+(4\cdot \frac{\sqrt{2}}{2})+(4\cdot \frac{1}{2})+...").scale(0.7).next_to(dot1, 0.1*RIGHT)
		solution1 = MathTex(r"S_{\infty }=\frac{4}{1-\frac{\sqrt{2}}{2}}").scale(0.7).next_to(dot2, 0.1*RIGHT)
		solution2 = MathTex(r"=8+4\sqrt{2}").scale(0.7).next_to(dot3, 0.1*RIGHT)

		self.play(Write(solution))
		self.wait()
		self.play(TransformFromCopy(solution, solution1))
		self.wait()
		self.play(TransformFromCopy(solution1, solution2))
		self.wait()







































