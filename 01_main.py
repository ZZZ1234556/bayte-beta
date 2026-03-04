from openai import OpenAI
from dotenv import load_dotenv
from agent import Agent

load_dotenv()

print("Byte.beta")

client = OpenAI()
agent = Agent()

while True:
    user_input = input("Tú: ").strip()
    
    # Validaciones
    if not user_input:
        continue
    
    if user_input.lower() in ("salir", "exit", "bye", "sayonara"):
        print("Hasta luego!")
        break
    
    # Agregar mensaje del usuario
    agent.messages.append({"role": "user", "content": user_input})
    
    # 🔥 OPTIMIZACIÓN: Limitar historial
    agent.messages = agent.messages[-6:]
    
    print("Byte:", end=" ", flush=True)

    with client.responses.stream(
        model="gpt-5-nano",
        input=agent.messages,
    ) as stream:

        for event in stream:
            if event.type == "response.output_text.delta":
                print(event.delta, end="", flush=True)

    print()  # salto de línea
