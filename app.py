import streamlit as st
import pandas as pd
from groq import Groq  # Assuming GroqClient is the correct class to import

# Streamlit app
st.set_page_config(
    page_title="Codebook for Global Student Learnning Outcomes",
    page_icon=":blue_heart:", 
    layout="wide",

)
st.write("## Codebook for Global Student Learnning Outcomes")
st.write(":blue_heart: **by JTIAPBN.Ai**")

# Global Citizen Codebook data

codebook_data = {
    "AD": [
        {"code": "1-AD", "outcome": "Awareness of how one's life and the lives of others are influenced by broader cultural and historical contexts", "description": "Making a connection between the historical past and the present culture; Acknowledging connections between one's life and the culture(s) in which one has grown up and/or the historical moment in which one lives; Acknowledging that actions taken in the past influence the way people are living today; Recognizing that cultural and/or historical components make up one's own identity and those of others"},
        {"code": "2-AD", "outcome": "Awareness of one's culture (behaviors, identity, beliefs)", "description": "Demonstrating familiarity with one's cultural identifiers (behaviors, identity, beliefs); Noticing one has a culture; Situating oneself in relation to culture"},
        {"code": "3-AD", "outcome": "Awareness of one's city and how it relates to other cities around the world", "description": "Recognizing there are differences between another student's lived experience in their city and one's own; Comparing aspects of one's own city (e.g., culture, technology, local environment, environmental issues, etc.) to those of another city"},
        {"code": "4-AD", "outcome": "Awareness of different cultures within one's school, city, region, country, and world", "description": "Recognizing that there are different cultures within one's school, city, region, country, and world; Acknowledging that there are connections and comparisons between different cultures within one's school, city, region, country, and world"},
        {"code": "5-AD", "outcome": "Awareness of one's identity as a citizen of one's city", "description": "Acknowledging one's role as a citizen of one's city beyond simply naming where one lives; Expressing a sense of responsibility (\"I must\"); Expressing a sense of belonging"},
        {"code": "6-AD", "outcome": "Ability to identify and critically reflect on stereotypes in thinking about others", "description": "Noticing and naming stereotypes and the impact of these stereotypes on people and communities; Asking critical questions and/or naming criticisms about stereotypes to oneself, one's community, and/or one's online peers; Reflecting on one's own bias; Articulating why prejudices should be rejected"},
        {"code": "7-AD", "outcome": "Ability to listen to others and discuss issues in a respectful and unbiased way", "description": "Giving a response that shows evidence of careful listening, reading, or observing through respectful discussion of issues"},
        {"code": "8-AD", "outcome": "Ability to ask questions when encountering different perspectives", "description": "Asking questions to learn more about a peer's life, place, and/or culture; Expressing a desire to learn more—and even visit; Asking questions that suggest how someone else's post gave them a new perspective or new information"},
        {"code": "9-AD", "outcome": "Ability to identify and critically reflect on bullying behavior online and in-person", "description": "Noticing and naming bullying behavior online and/or sharing instances of noticing and naming bullying behavior in-person; Asking critical questions and/or naming criticisms of online and/or in-person bullying behavior"},
        {"code": "10-AD", "outcome": "Positive attitude towards one's own culture", "description": "Expressing pride in and/or enthusiasm about one's own culture and/or place"},
        {"code": "11-AD", "outcome": "Tolerance of differences", "description": "Making explicit reference to differences among people with neither positivity nor negativity; Expressing openness to content and/or perspectives shared by another student or responding in respectful ways to differences without expressing explicit positivity"},
        {"code": "12-AD", "outcome": "Responding to differences with openness and positivity, not fear", "description": "Making explicit, positive reference to differences among people; Responding to these differences with inclusive and collaborative language; Expressing an appreciation for diverse perspectives and places; Expressing excitement or enthusiasm for the diverse content and/or perspectives shared by another student"},
        {"code": "13-AD", "outcome": "Willingness to interact with peers and adults of different backgrounds respectfully", "description": "Articulating a willingness to interact with peers and adults of different backgrounds respectfully"},
        {"code": "14-AD", "outcome": "Willingness to work collaboratively with peers and adults of different backgrounds to achieve shared goals", "description": "Expressing a willingness to work collaboratively with others (peers or adults) to achieve shared goals"},
        {"code": "15-AD", "outcome": "Interacting with people of different backgrounds positively and respectfully", "description": "Responding in respectful and positive ways to peers from different places"},
        {"code": "16-AD", "outcome": "Working collaboratively with people of different backgrounds to achieve shared goals", "description": "Describing actions one has taken or is taking to work collaboratively with students or others in one's community toward specific goals"},
        {"code": "17-AD", "outcome": "Intervening against intolerant behavior online and in-person", "description": "Actively intervening against intolerant behavior online; Describing ways in which one intervenes against intolerant behavior online and/or in-person"}
    ],
    "CU": [
        {"code": "18-CU", "outcome": "Understanding how one's life and the lives of others are influenced by broader cultural and historical contexts", "description": "Explaining or describing how or why actions taken in the past influence the way people are living or why things are as they are in the world today; Recognizing that cultural and/or historical components make up one's own identity and/or those of one's peers"},
        {"code": "19-CU", "outcome": "Understanding of one's culture (behaviors, identity, beliefs)", "description": "Explicitly defining one's culture by explaining cultural aspects (behavior, identity, beliefs); Expressing nuanced beliefs/opinions about one's own culture (positive and critical within the same post); Differentiating between what is and/or what is not one's own \"culture\""},
        {"code": "20-CU", "outcome": "Understanding of one's city and how it relates to other cities around the world", "description": "Explaining explicit connections and comparisons between another student's lived experience in their city and one's own; Naming similarities and/or differences between culture, technology, local environment, environmental issues, etc."},
        {"code": "21-CU", "outcome": "Understanding of different cultures within one's school, city, region, country, and world", "description": "Analyzing different cultures within one's school, city, region, country, and/or world; Explaining connections, similarities, and/or differences between different cultures within one's school, city, region, country, and/or world"},
        {"code": "22-CU", "outcome": "Understanding that problems may be solved differently depending on cultural factors", "description": "Naming or explaining how cultural differences affect approaches to problem solving; Acknowledging or explaining how one can use information, opinions, and contexts derived from cultural learning to understand different perspectives on problems and develop solutions"},
        {"code": "23-CU", "outcome": "Ability to adapt language and content of writing to meet the needs of diverse audiences", "description": "Providing translations for words; Explaining the meaning of words or phrases; Making a comparison between something that is likely unfamiliar and something they think others will be familiar with; Attempting to explain or describe in words something another person has never experienced before or would likely be unfamiliar with; Reporting adapting language or content as part of engaging with different audiences through any medium, including translation"},
        {"code": "24-CU", "outcome": "Ability to recognize different perspectives on specific global issues", "description": "Naming and acknowledging different perspectives that exist in the world, such as in their community, in the media, or among experts"},
        {"code": "25-CU", "outcome": "Recognition of different perspectives as legitimate", "description": "Naming and acknowledging different perspectives that exist in the world as valid, fair, reasonable, supported by tradition, custom, or standard"},
        {"code": "26-CU", "outcome": "Positive attitude towards other cultures", "description": "Expressing positive attitudes towards other cultures at any point"}
    ],
    "GK": [
        {"code": "27-GK", "outcome": "Knowledge of local and world geography", "description": "Sharing facts and information about and/or showing one's understanding of local and world geography"},
        {"code": "28-GK", "outcome": "Knowledge of global issues and their local impact", "description": "Acknowledging connections between global issues and their local impacts; Noting the ways in which local behaviors affect global issues"},
        {"code": "29-GK", "outcome": "Knowledge of economics and politics and their impact", "description": "Sharing information about and showing understanding of economics and/or politics and their impact"},
        {"code": "30-GK", "outcome": "Knowledge of one's city government and differences between city governments around the world", "description": "Sharing information about and showing one's understanding of the structure and workings of one's own city government; Making comparative statements about other city governments"},
        {"code": "31-GK", "outcome": "Understanding that global issues are borderless and affect everyone", "description": "Naming or explaining ways in which global issues are borderless and affect multiple people, places, and species"},
        {"code": "32-GK", "outcome": "Understanding that global issues are complex", "description": "Noting complexity of global issues; Recognizing and identifying the challenges of finding, planning, and implementing viable solutions to global issues; Acknowledging and/or grappling with personal lifestyle/enjoyment versus environmental or social responsibility; Proposing solutions to issues at different levels—individual solutions, neighborhood solutions, infrastructure solutions, etc.; Recognizing that multiple systems are involved/at play and/or explaining explicit ways systems interact (intercity; local-global)"},
        {"code": "33-GK", "outcome": "Understanding that differences in access to information, technology, and resources affect quality of life and perspectives", "description": "Acknowledging there are varying levels of access to information, technology, and resources; Making connections between one's access and others' access and connecting that to quality of life and/or perspectives"},
        {"code": "34-GK", "outcome": "Understanding that problems may be solved differently depending on socioeconomic status, natural resources, government policy, and political differences", "description": "Naming or explaining specific ways in which solutions to problems may differ based on (i) socioeconomic status of communities implementing solutions, (ii) natural resources in the local area, and/or (iii) government policies and political differences"},
        {"code": "35-GK", "outcome": "Ability to apply research skills (finding, selecting, and applying information from multiple sources) to global issues", "description": "Describing research processes that can be broadly described as finding, selecting, and applying existing information, be this from primary and/or secondary sources"},
        {"code": "36-GK", "outcome": "Ability to find information about global issues using credible sources from around the world", "description": "Citing or sharing information about global issues from multiple credible sources"},
        {"code": "37-GK", "outcome": "Ability to synthesize different perspectives on the same topic to draw conclusions about global issues", "description": "Distilling information from different sources/perspectives to develop an argument or make a claim about global issues, drawing on evidence as needed"},
        {"code": "38-GK", "outcome": "Recognition of the importance of learning about other cities and countries", "description": "Acknowledging that it is important to learn about other cities and countries"},
        {"code": "39-GK", "outcome": "Recognition of the importance of learning about global issues that affect us all", "description": "Acknowledging that it is important to learn about global issues that affect us all"},
        {"code": "40-GK", "outcome": "Recognition of the importance of analyzing multiple perspectives", "description": "Naming specific reasons why analyzing multiple perspectives is important; Expressing positivity relating to recognizing multiple perspectives or mentioning the value of weighing different forms of input or perspectives"}
    ],
    "GE": [
        {"code": "41-GE", "outcome": "Ability to engage in inclusive problem solving", "description": "Describing ways in which they have actually sought opportunities to communicate with people in other cities and/or cultures or with people in their own city/culture"},
        {"code": "42-GE", "outcome": "Interest in the larger world, particularly unfamiliar people and places", "description": "Expressing curiosity about the larger world, including unfamiliar people and places"},
        {"code": "43-GE", "outcome": "Interest in global issues", "description": "Expressing curiosity and wanting to know more about global issues"},
        {"code": "44-GE", "outcome": "Recognition of the value of inclusive problem-solving", "description": "Articulating the importance of inclusive problem solving"},
        {"code": "45-GE", "outcome": "Recognizing one's capacity to advocate for and contribute to local, regional, or global improvement", "description": "Recognizing one's capacity to advocate for and/or contribute to local, regional, or global improvement; Expressing a sense of efficacy in relation to participating in advocacy and other social change efforts at the local, regional, and/or global levels"},
        {"code": "46-GE", "outcome": "Appreciation of language learning as a means of communicating and collaborating with people around the world", "description": "Explicitly acknowledging the value of language learning as a means of communicating and collaborating with people around the world"},
        {"code": "47-GE", "outcome": "Willingness to take action to address global issues", "description": "Indicating a desire and clear intention on the part of the student to take action, make changes, and/or solve problems"},
        {"code": "48-GE", "outcome": "Using digital tools to learn from and communicate with students from cities around the world", "description": "Sharing evidence of using digital tools or describing having used or using digital tools to learn from and/or communicate with students from cities around the world"},
        {"code": "49-GE", "outcome": "Seeking opportunities to communicate with people in other cities and cultures, as well as one's own", "description": "Describing ways in which they have actually sought opportunities to communicate with people in other cities and/or cultures or with people in their own city/culture"},
        {"code": "50-GE", "outcome": "Seeking opportunities to interact and collaborate with people of different cultures and backgrounds", "description": "Describing ways in which one seeks opportunities to collaborate with people of different cultures and/or backgrounds"},
        {"code": "51-GE", "outcome": "Gathering and interpreting information from people in one's own city and culture", "description": "Describing the processes of collecting information and content of data/information collected from people in one's city or culture"},
        {"code": "52-GE", "outcome": "Gathering and interpreting information from people in other cities and cultures", "description": "Describing the process of collecting information and content of data/information collected from people in other cities and cultures"},
        {"code": "53-GE", "outcome": "Presenting information, formally and informally, to people in one's own city and culture", "description": "Sharing evidence from presentations of information or describing specific ways in which one is sharing or presenting information with other people outside one's classroom but within one's city and/or culture"},
        {"code": "54-GE", "outcome": "Presenting information, formally and informally, to people in other cities and cultures", "description": "Sharing evidence of presentations of information or describing specific ways in which one is sharing or presenting information with other people in other cities and/or cultures"},
        {"code": "55-GE", "outcome": "Working to contribute to local, regional, or global improvement", "description": "Describing projects or actions that have been or are currently being implemented and that seek to resolve issues at the local, regional, or global levels"}
    ]
}



# Function to call the Groq API using the package
def generate_content(api_key, codebook, characteristic):
    client = Groq(api_key=api_key) 
    # Initialize the client with the API key
    try:
        content = client.chat.completions.create(messages=[
                {"role": "system", "content":  f"You are an expert in global citizenship education. match the relevent codes, outcomes, and descriptions in a table format based from the following codebook:{codebook} of the following students characteristic:{characteristic}."}, 
                ],
                max_tokens=4096, model= llm_model)
        return content
    except Exception as err:
        st.error(f"Error occurred: {err}")
        return None



# User inputs
api_key = st.sidebar.text_input("Enter your Groq API key:", type="password")
llm_model= st.sidebar.selectbox("Select Model:",options= ["llama3-70b-8192","llama3-8b-8192", "mixtral-8x7b-32768"])
characteristic = st.sidebar.text_area("Enter desired characteristic:", height=100)
codebook=codebook_data

if st.sidebar.button("Generate"):
    if not api_key:
        st.sidebar.error("Please enter your Groq API key.")
    else:
        with st.spinner("Mapping your characteristic..."):
            content = generate_content(api_key, codebook, characteristic)
            if content:
                st.write( f"{content.choices[0].message.content}")


if __name__ == "__main__":

    st.sidebar.header("About")
    st.sidebar.info(
        "This app uses AI to analyze student characteristics and suggest relevent"
        "outcomes from the Global Citizen Codebook. It helps educators identify"
        "areas of global competence that align with their student's traits and experiences.\n\n"
        "Reference: https://www.globalcities.org/codebook"
    )

    st.sidebar.header("How to use")
    st.sidebar.info(
        "1. Enter your Groq API key in the text box on the left.\n"
        "2. Select the model you want to use.\n"
        "3. Enter your student characteristic in the text area on the left.\n"
        "4. Click the 'Generate' button to get the suggested outcomes.\n\n"
        "Note: Your API key is used only for this session and is not stored.\n"
    )
