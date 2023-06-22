import streamlit as st
import random

def main():
    st.title("Гра 'Вгадай число'")
    secret_number = random.randint(1, 10)

    guess = st.number_input('Введіть число', min_value=1, max_value=10, step=1)
    result_message = ""

    if st.button('Перевірити'):
        if guess == secret_number:
            result_message = "Ви вгадали число!"
        else:
            result_message = f"Неправильно. Загадане число: {secret_number}"

    st.write(result_message)

if __name__ == '__main__':
    main()


