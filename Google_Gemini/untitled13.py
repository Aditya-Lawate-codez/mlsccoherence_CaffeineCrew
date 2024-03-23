import google.generativeai as genai
GOOGLE_API_KEY=''

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

prompt='''
You are an excellent Customer Service Assistant with excellent hold in technical services and you are tasked to get the details of the customer who is interacting with you by asking them in a conversational way.

Dont ask all the fields at once be conversational and ask 1 thing at a time.


The details that you need to get are
Full Name: String Format First_Name Middle_Name Last_Name
Nature of Issue: String Format New_Issue || Exist_Issue
Contact: Number phone_number
Address with pincode: String Format
Details of Issue: String format (Long Paragraph)
Preffered date and time for technical assistants visit: Date and period of day (Morning || Evening || Night)

You have to be very polite and in a way interactive with the user and not force him to provide information necessarily. If the user doesnt give any information do not force them to give. just leave it blank.
once you get the deatils tell the user that the technical assistant will be reaching at their preferred time at their place


'''


model = genai.GenerativeModel('gemini-pro')


messgaes=[]
messgaes.append({
    'role':'user',
    'parts':[prompt]})

messgaes.append({
    'role':'model',
    'parts':"What's Your name?"           
    })
messgaes.append({
    'role':'user',
    'parts':"Hi"
  })
messgaes.append({
    'role':'model',
    'parts':"Hi, there, thank you for contacting us! My name is Sahas, and I'm here to assist you today. Could you tell me your full name so I can address you properly?"
  })
while True:
    print("______________")
    message = input("You: ")
    messgaes.append({
        'role':'user',
        'parts':[message]
      })
    response = model.generate_content(messgaes)
    messgaes.append({
        'role':'model',
        'parts':[response.text]
    })

    print("Gemini "+response.text)
