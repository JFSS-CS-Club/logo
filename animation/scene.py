from manim import *


class AnimateLogo(Scene):
    def construct(self):
        logo = Tex("\\hspace{3em}C", "lub \\\\", "JFS", "S").set_color(BLUE)
        logoBg = logo.copy().set_color(WHITE)
        # Make it look like the entirety of Club is being written
        logoBg[0].set_color(BLUE)
        group = VGroup(logo, logoBg)
        group.set_width(config["frame_width"] - 2 * LARGE_BUFF)
        self.play(Write(logoBg[2:4]))
        self.play(Write(logo[::len(logo)-1]))
        self.play(Write(logoBg[0:2]))
        self.remove(logoBg[3], logoBg[0])   # Remove unneeded logo parts
        self.wait()
        self.play(FadeOutAndShift(logoBg[1:3]),
                  FadeOutAndShift(logo[::len(logo)-1]))
        self.wait()
