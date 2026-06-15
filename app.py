import gradio as gr
from query import ask


def handle_query(question):
    if not question.strip():
        return "Please enter a question.", ""

    result = ask(question)

    answer = result["answer"]
    sources = "\n".join(f"- {source}" for source in result["sources"])

    return answer, sources


with gr.Blocks() as demo:
    gr.Markdown("# Unofficial Minecraft Survival Guide")
    gr.Markdown("Ask a Minecraft survival question and get an answer based on your collected documents.")

    question = gr.Textbox(
        label="Your question",
        placeholder="Example: What should I do on my first day in Minecraft?"
    )

    ask_button = gr.Button("Ask")

    answer = gr.Textbox(label="Answer", lines=8)
    sources = gr.Textbox(label="Sources", lines=4)

    ask_button.click(
        handle_query,
        inputs=question,
        outputs=[answer, sources]
    )

    question.submit(
        handle_query,
        inputs=question,
        outputs=[answer, sources]
    )

demo.launch()