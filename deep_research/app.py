import gradio as gr
from dotenv import load_dotenv

from research_manager import ResearchManager
from styles import CSS, JS, EXAMPLES, HEADER_HTML

load_dotenv(override=True)


async def run(query: str):

    query = query.strip()

    if not query:
        yield "⚠️ Please enter a research topic."
        return

    manager = ResearchManager()

    async for status_update in manager.run(query):
        yield status_update



with gr.Blocks(
    title="PRISMA AI - Prajwal K.C.",
    css=CSS,
    js=JS,
    theme=gr.themes.Base()
) as ui:


    # Header
    gr.HTML(HEADER_HTML)


    # Main input section
    with gr.Row(elem_classes="prisma-query-row"):

        query_box = gr.Textbox(
            placeholder="Ask PRISMA AI to research any topic...",
            show_label=False,
            container=False,
            autofocus=True,
            elem_id="prisma-query",
            scale=5,
            lines=1
        )


        launch_button = gr.Button(
            "🚀 Launch Research",
            variant="primary",
            elem_id="prisma-run",
            scale=1
        )


    # Example prompts

    gr.HTML(
        """
        <div class="example-title">
        EXPLORE WITH PRISMA AI
        </div>
        """
    )


    gr.Examples(
        examples=EXAMPLES,
        inputs=query_box,
        elem_id="prisma-examples"
    )


    # Output

    gr.Markdown(
        """
        <div class="report-title">
        Research Output
        </div>
        """
    )


    report = gr.Markdown(
        elem_id="prisma-report"
    )


    launch_button.click(
        fn=run,
        inputs=query_box,
        outputs=report
    )


    query_box.submit(
        fn=run,
        inputs=query_box,
        outputs=report
    )



if __name__ == "__main__":
    ui.launch()