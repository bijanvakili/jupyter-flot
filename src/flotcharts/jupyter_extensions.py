from __future__ import print_function
import json
from IPython.display import display, Javascript, HTML


DEFAULT_FLOT_JS = 'https://cdnjs.cloudflare.com/ajax/libs/flot/0.8.3/jquery.flot.min.js'
DEFAULT_CSS = """
    width: 100%;
    height: 400px;
    font-size: 14px;
    line-height: 1.2em;
"""

class FlotCharts:
    PLACEHOLDER_STYLENAME = "flotmagic-placeholder"

    def __init__(self, flotjs=None, css_placeholder=None):
        self.url_flotjs = flotjs or DEFAULT_FLOT_JS
        self.css_placeholder = css_placeholder or DEFAULT_CSS
        self.chart_counter = 0

    def setup(self):
        display(
            Javascript(data="""$.getScript('{0}')""".format(self.url_flotjs))
        )

    def plot(self, data, css=None):
        self.chart_counter += 1
        placeholder_id = 'placeholder{0}'.format(self.chart_counter)

        if not css:
            css = self.css_placeholder
        placeholder = HTML(
            """
            <style>
            .{style_name} {{
                {style_content}
            }}
            </style>
            <div id="{placeholder_id}" class="{style_name}"></div>
            """.format(
                style_name=self.PLACEHOLDER_STYLENAME,
                style_content=css,
                placeholder_id=placeholder_id
            )
        )
        plot_command = Javascript(
            '$.plot("#{placeholder_id}", {data});'.format(
                placeholder_id=placeholder_id,
                data=json.dumps(data)
            )
        )
        display(*[placeholder, plot_command])
