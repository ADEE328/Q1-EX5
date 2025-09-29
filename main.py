from pyscript import document

def generate_message(e):
   
    name = document.getElementById('text1').value
    age = document.getElementById('text2').value
    school = document.getElementById('text3').value

    message = f"""
Student Profile
Name   : {name}
Age    : {age}
School : {school}

Notes:
{name} is currently {age} years old and studies at {school}.
"""
    document.getElementById("output-area").innerText = message
