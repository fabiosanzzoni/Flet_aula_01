import flet as ft

def main(page: ft.Page):

    page.title = "Lista de Tarefas Infinity"
    page.padding = 10

    lista_tarefas = ft.Column()

    campo_tarefa = ft.TextField(
        label="Digite a tarefa: ",
    )

    def adicionar_tarefa(e):
        if campo_tarefa.value.strip() == "":
            campo_tarefa.value = "Escreva o nome da tarefa!"

        nova_tarefa = ft.Row([
            ft.Text(campo_tarefa.value),
        ])

        lista_tarefas.controls.append(nova_tarefa)

        campo_tarefa.value = ""

        page.update()

    botao_adicionar = ft.ElevatedButton(
        "Adicionar Tarefa",
        on_click=adicionar_tarefa
    )

    page.add(
        ft.Row([campo_tarefa, botao_adicionar], alignment=ft.MainAxisAlignment.CENTER),
        lista_tarefas
    )

ft.app(target=main)