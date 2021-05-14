"""Testando o que aprendi no Curso de Python."""

from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: '))

    calc: Calcular = Calcular(dificuldade)

    print('Possuímos a seguinte operação: ', end='')
    calc.mostrar_operacao()

    resultado: int = int(input('Informe o resultado: '))

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você possui {pontos}')
        continuar: int = int(input('Deseja continuar no Jogo? [1]Sim [0]Não -> '))
        if continuar:
            jogar(pontos)
        else:
            print(f'Você encerrou o Game com {pontos} pontos.')
            print('Até a próxima! :D')


if __name__ == '__main__':
    main()
