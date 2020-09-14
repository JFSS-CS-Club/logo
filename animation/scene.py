from manim import *

class TextToLogo(Scene):
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

class AnimateLogo(Scene):
    def construct(self):
        logoA = TextMobject("\\hspace{3em}C", "lub \\\\", "JFS", "S")
        logoB = TextMobject("\\hspace{3em}\\textbf{C}", "lub \\\\","JFS", "\\textbf{S}")
        logoC = logoB.deepcopy()
        self.play(Write(logoA[2:4]))
        self.play(Write(logoB[::len(logoB)-1]), Transform(logoA[2:3], logoB[2:3]))
        self.play(Write(logoC[0:2]), FadeOut(logoA[3]))
        self.play(FadeOut(logoA[2:3]), FadeOut(logoB[::len(logoB)-1]), FadeOut(logoC[0:2]))
        self.wait()