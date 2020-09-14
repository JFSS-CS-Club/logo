from manim import *

class AnimateLogo(Scene):
    def construct(self):
        logoA = TextMobject("\\hspace{3em}C", "lub \\\\", "JFS", "S")
        logoB = TextMobject("\\hspace{3em}\\textbf{C}", "lub \\\\","JFS", "\\textbf{S}")
        logoC = logoB.deepcopy()
        self.play(Write(logoA[2:4]))
        self.play(Write(logoB[::len(logoB)-1]), ReplacementTransform(logoA[2], logoB[2]))
        self.play(Write(logoC[0:2]), FadeOut(logoA[3]))
        self.play(FadeOut(logoA[2:3]), FadeOut(logoB[::len(logoB)-1]), FadeOut(logoC[0:2]))
        self.wait()

class AnimateLogoSlogan(Scene):
    def construct(self):
        logoUnbolded = TextMobject("\\hspace{3em}C", "lub \\\\", "JFS", "S")
        logoBolded = TextMobject("\\hspace{3em}\\textbf{C}", "lub \\\\","JFS", "\\textbf{S}")
        slogan = TextMobject("What will you build?")
        self.play(Write(logoUnbolded[2:4]))
        self.play(Write(logoBolded[::len(logoBolded)-1]), ReplacementTransform(logoUnbolded[2], logoBolded[2]), FadeOut(logoUnbolded[3]))
        self.play(Write(logoBolded[1]))
        self.wait()
        self.play(ReplacementTransform(logoBolded, slogan))
        self.wait()
        self.play(FadeOut(slogan))
        self.wait()

class AnimateLogoSloganNoFade(Scene):
    def construct(self):
        logo = TextMobject("\\hspace{3em}\\textbf{C}", "lub \\\\", "JFS", "\\textbf{S}")
        logoWriteable = logo.copy()
        slogan = TextMobject("What will you build?")
        text = logo.copy()
        self.add(text)
        self.play(Write(logoWriteable[2:4]))
        self.play(Write(logoWriteable[::len(logoWriteable)-1]))
        self.play(Write(logoWriteable[0:2]))
        self.play(FadeOut(logoWriteable), run_time=0.01)
        self.wait(1)
        self.play(Transform(text, slogan))
        self.wait(2)
        self.play(Transform(text, logo))