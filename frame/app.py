from sufficient.frames import *


class App:
    name = "GM Universe"
    description = "A boilerplate for creating frame apps"
    image = "{uri}/static/home.svg"
    uri = "{uri}"
    start = "PageHome"


class PageHome:
    def view(self, action: Action, result: ActionResult):
        return SvgFile("home.svg")

    def btn_normal_button(self, action: Action):
        return "PageNext"

    def goto_redirect_button(self, action: Action):
        return "https://github.com/briceyan/frame-app-boilerplate"

    def input_input_text(self, action: Action):
        # wip
        pass


class PageNext:
    def view(self, action: Action, result: ActionResult):
        return SvgImageView.from_string(SvgTemplate("PageNext", "hello"))

    def btn_prev(self, action: Action):
        return "PageHome"

    def btn_refresh(self, action: Action):
        return "PageNext"


def SvgTemplate(title, content):
    return f"""<svg width="640" height="336" xmlns="http://www.w3.org/2000/svg">
  <foreignObject width="100%" height="100%">
    <body xmlns="http://www.w3.org/1999/xhtml">
      <h1>{title}</h1>
      <p>{content}</p>
    </body>
  </foreignObject>
</svg>
"""
