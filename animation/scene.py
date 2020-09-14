from manim import *

class AnimateLogo(Scene):
    # def construct(self):
    #     logoCS = TextMobject('\\textbf{C \\\\ S}')
    #     logoTop = TextMobject('Club')
    #     logoBottom = TextMobject('JFSS')
    #     VGroup(logoTop, logoBottom).arrange(DOWN)
    #     self.play(Write(logoTop))
    #     self.play(Write(logoBottom))
    #     self.play(
    #             ApplyMethod(logoTop.shift, 0.5*RIGHT),
    #             ApplyMethod(logoBottom.shift, 0.5*LEFT)
    #     )
    def construct(self):
        logoStart = TextMobject("JFSS CS Club")
        logoEnd = TextMobject("\\hspace{3em}\\textbf{C}lub \\\\ JFS\\textbf{S}")
        self.play(Write(logoStart))
        self.wait()
        self.play(Transform(logoStart, logoEnd))
        self.wait()
        self.play(FadeOut(logoStart))
        self.wait()