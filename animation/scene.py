from manim import *


class AnimateLogoSlogan(Scene):
    def construct(self):
        logoUnbolded = TextMobject("\\hspace{3em}C", "lub \\\\", "JFS", "S")
        logoBolded = TextMobject("\\hspace{3em}\\textbf{C}", "lub \\\\","JFS", "\\textbf{S}")
        slogan = TextMobject("What will you build?")
        group = VGroup(logoUnbolded, logoBolded, slogan)
        group.set_width(config["frame_width"] - 2 * LARGE_BUFF)
        self.play(Write(logoUnbolded[2:4]))
        self.play(Write(logoBolded[::len(logoBolded)-1]), ReplacementTransform(logoUnbolded[2], logoBolded[2]), FadeOut(logoUnbolded[3]))
        self.play(Write(logoBolded[1]))
        self.wait()
        self.play(ReplacementTransform(logoBolded, slogan))
        self.wait()
        self.play(FadeOut(slogan))
        self.wait()
