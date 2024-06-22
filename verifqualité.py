import tkinter as tk
from tkinter import ttk
import openai

class ServiceEvaluationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Évaluation de la Performance du Service")

        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.create_widgets()

    def create_widgets(self):
        performance_label = ttk.Label(self.main_frame, text="Performance du Service:")
        performance_label.grid(column=0, row=0, sticky=tk.W)
        self.performance_scale = ttk.Scale(self.main_frame, from_=1, to=10, orient=tk.HORIZONTAL)
        self.performance_scale.grid(column=1, row=0)

        quality_label = ttk.Label(self.main_frame, text="Qualité du Service:")
        quality_label.grid(column=0, row=1, sticky=tk.W)
        self.quality_scale = ttk.Scale(self.main_frame, from_=1, to=10, orient=tk.HORIZONTAL)
        self.quality_scale.grid(column=1, row=1)

        efficiency_label = ttk.Label(self.main_frame, text="Efficacité du Service:")
        efficiency_label.grid(column=0, row=2, sticky=tk.W)
        self.efficiency_scale = ttk.Scale(self.main_frame, from_=1, to=10, orient=tk.HORIZONTAL)
        self.efficiency_scale.grid(column=1, row=2)

        comments_label = ttk.Label(self.main_frame, text="Commentaires:")
        comments_label.grid(column=0, row=3, sticky=tk.W)
        self.comments_entry = tk.Text(self.main_frame, width=30, height=5)
        self.comments_entry.grid(column=1, row=3)

        submit_button = ttk.Button(self.main_frame, text="Soumettre", command=self.submit_form)
        submit_button.grid(column=1, row=4, pady=10)

        self.result_text = tk.StringVar()
        result_label = ttk.Label(self.main_frame, textvariable=self.result_text, wraplength=300)
        result_label.grid(column=0, row=5, columnspan=2)

    def submit_form(self):
        try:
            performance_score = self.performance_scale.get()
            quality_score = self.quality_scale.get()
            efficiency_score = self.efficiency_scale.get()
            comments = self.comments_entry.get("1.0", tk.END)

            user_input = f"Performance: {performance_score}, Qualité: {quality_score}, Efficacité: {efficiency_score}, Commentaires: {comments}"
            response = openai.Completion.create(
                engine="davinci-codex",
                prompt=user_input,
                max_tokens=50,
                n=1,
                stop=None
            )

            self.result_text.set(response.choices[0].text.strip())

        except Exception as e:
            self.result_text.set("Une erreur est survenue lors de la génération de la réponse.")
            print(f"Erreur lors de l'appel à l'API : {str(e)}")

if __name__ == "__main__":
    openai.api_key = 'sk-proj-CUG8Up4ubU6GDX6YRin0T3BlbkFJ66hAO6vaN4ObXAGyUNew'
    root = tk.Tk()
    app = ServiceEvaluationApp(root)
    root.mainloop()
