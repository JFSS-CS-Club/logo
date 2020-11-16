from manim import *


class AnimateLogo(Scene):
    def construct(self):
        logo = Tex("\\hspace{3em}C", "lub \\\\", "JFS", "S")
        logoGrey = logo.copy().set_color("#AAAAAA")
        # Make it look like the entirety of Club is being written
        logoGrey[0].set_color(WHITE)
        group = VGroup(logo, logoGrey)
        group.set_width(config["frame_width"] - 2 * LARGE_BUFF)
        self.play(Write(logoGrey[2:4]))
        self.play(Write(logo[::len(logo)-1]))
        self.play(Write(logoGrey[0:2]))
        self.remove(logoGrey[3], logoGrey[0])   # Remove unneeded logo parts
        self.wait()
        self.play(FadeOutAndShift(logoGrey[1:3]),
                  FadeOutAndShift(logo[::len(logo)-1]))
        self.wait()
