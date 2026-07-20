import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager

load_dotenv(override=True)


async def run(query: str):
    """
    Execute the Deep Research workflow.
    """

    query = query.strip()

    if not query:
        yield "# Please enter a research topic."
        return

    manager = ResearchManager()

    async for update in manager.run(query):
        yield update


with gr.Blocks(
    title="Deep Research AI",
    theme=gr.themes.Soft()
) as ui:

    gr.Markdown(
        """
# 🔍 Deep Research AI

Plan research → Search the Web → Generate Report → Email Results
"""
    )

    query_textbox = gr.Textbox(
        label="Research Topic",
        placeholder="Example: Future of AI Agents in Healthcare",
        lines=2,
    )

    run_button = gr.Button(
        "🚀 Start Research",
        variant="primary",
    )

    report = gr.Markdown()

    run_button.click(
        fn=run,
        inputs=query_textbox,
        outputs=report,
    )

    query_textbox.submit(
        fn=run,
        inputs=query_textbox,
        outputs=report,
    )


if __name__ == "__main__":
    ui.launch()