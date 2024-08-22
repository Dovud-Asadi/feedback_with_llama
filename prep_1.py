import json
import string
from groq import Groq
import os

client = Groq(
    api_key="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", #cs
)

directory = 'unzipped_folder\data_new_filtered\folder_1'  # Raw string

system_message_modified = {
    "role": "system",
    "content": """
    Act as an IELTS Speaking examiner. You will be provided with transcripts of IELTS Speaking dialogues, which you must evaluate NEATLY based on all IELTS criteria. The criteria include: Fluency and Coherence, Lexical Resource, Grammatical Range and Accuracy, and Pronunciation. Consider the provided Pronunciation Assessment for Pronunciation evaluation.

    For each criterion, assign a score from 0 to 9. Calculate the EXACT overall band score based on the four criteria of the IELTS Speaking exam. Additionally, provide concise feedback STRICTLY following the rules outlined below:

    1. Personalize your feedback and make it specific to the candidate's performance.
    2. Mention specific mistakes.
    3. Evaluate Fluency and suggest how it could be improved.
    4. Assess the use of Lexical Resource, quoting specific parts where improvements with alternatives and collocations are possible.
    5. Carefully examine the transition and flow between ideas, suggesting better usage of cohesive devices.

    Ensure you FOLLOW the PROVIDED FINAL OUTPUT STRUCTURE for your evaluation. The overall band score must be separated into the four aspects: FLUENCY, VOCABULARY, GRAMMAR, and PRONUNCIATION. This structure should only be followed if the conversation contains all 3 complete parts. The transcript structure is as follows:

    - examiner: <questions by examiner>
    - candidate: <answered voice transcript>

    If provided, include the pronunciation_assessment at the end:
    pronunciation_assessment:
    - pronunciation_score: <float> out of 100
    - accuracy_score: <float> out of 100
    - fluency_score: <float> out of 100
    - completeness_score : <float> out of 100
    - mispronounced_words: <list of words>

    Final output structure:
    Feedback: <Feedback>

    Band score: <Overall Band Score>
    Fluency: <Fluency Score>
    Vocabulary: <Vocabulary Score>
    Grammar: <Grammar Score>
    Pronunciation: <Pronunciation Score>

    Specific topic-words used by the candidate (worth mentioning):

    Suggested less used topic-related words, idioms, or collocations:

    Transcript Structure:
    ------------------ part_1 ---------
    - examiner: <questions by examiner>
    - candidate: <answered voice transcript>
    ------------------ part_2 ---------
    - examiner: <questions by examiner>
    - candidate: <answered voice transcript>
    ------------------ part_3 ---------
    - examiner: <questions by examiner>
    - candidate: <answered voice transcript>
    """
}

content_user = """
------------------ part_1 ---------
- examiner: How often do you wear jewelry?.
 candidate: well I really like to wear jewelry it just can complete your style and it's really it look very beautiful I can't go out without jewelry and always should be in my always should be I should wear the jewelry especially which my mom gave to me and also the complex complex
- examiner: What type of jewelry do you like to wear?.
 candidate: Well, I really like to wear the chain, bracelet and also the ring from the How to say it? Brilliant, huh? I really interested to wear the jewelry from the beasters
- examiner: Do you usually buy jewelery?.
 candidate: No, I don't like to buy the jewelry because I have the money only to the same jewelry and every time I lose this jewelry which I buy from myself. I never lose the jewelry which someone do present to me.
- examiner: Why do you think some people wear a piece of jewelry for a long time?.
 candidate: I don't know, it may be someone present, a really darling person present to them, this jewelry, or from this jewelry they can, they can, they can remain about something
------------------ part_2 ---------
- examiner: Describe an occasion when you got incorrect information.

 You should say:
 • why you need this information
 • how you got it
 • how you found it was incorrect
 • and how you felt about this experience..
 candidate: Well, I'm going to talk about the occasion when I got incorrect information. Well, it was 2 years ago when I was in the 9th grade and it was the exams after the school graduation exams and after that I should enter the university. Well, we had overall 20 exams but 14 exams was in between 6th of May and my friend said me no that time I haven't I hadn't my own mobile phone and my friend said me that the test exam started at 11. Guys, what do you think and I and this day is came and I went to the school and look there is the no one from the my class there is the another pure another pupils from the another class which they graduated 11th grade but 9th grade which there is no one my friend said me incorrect information at starting time it started at night and when when I came it's just ended I was very angry I don't I didn't know I should cry or smile I mean I should I think I thought that I saw that I should smile because I I wouldn't to I wouldn't to enter I wouldn't I hadn't the exams it was really difficult and what I want why I wanted to cry because I shouldn't to enter the university to you and to entering to university to this room you needed the paper which wrote you have done have done all your exams well what do you mean what do you think I lost the time and just I I shouldn't study at school 10th and 11th grade notice I'm in 11th grade I'm happy that I'm graduating I'm graduating and I believe I strongly believe that this year I will check the time of exams from myself I wouldn't believe to someone
------------------ part_3 ---------
- examiner: What is the difference between providing information by phone and by email?.
 candidate: Well, there is a lot of kinds of professions which related to giving information to others. For example, reporters. The reporters giving information about the news, about another countries, happening in the countries, to the people from the TV. And second is the teachers, teachers giving the knowledge, and they teach the students, and they give information which they know, and they wanted to be their students better than they. And third one is the doctors, especially actually doctors giving the information for the people who come them, who ill, they are write instructions and medicines, in what time, when they should drink their medicines, they write medicines which they can buy.
- examiner: How can people check whether a piece of information is correct or not?.
 candidate: The difference between providing information by phone and by mail is that by mail it's more easier because by mail you can just send text, send information to the people who you want. Not only one people, you can send it in the first time to ten or more people. It's so fast and more comfortable than by phone. These people check their email very fast. By phone it's more difficult than by email. By phone you should call by one person.
- examiner: Do people trust the information online?.
 candidate: Truth. Do people trust the information online? Yes, some people really do trust the information online. They not only trust the information online, they trust it just from the gaps or sentences they listen from other people. But in some cases, there are different people who don't believe the online and the people's sentences. They believe what they saw.
"""

content_assis = """
 "Feedback:\nThe candidate's responses show a basic level of communication with frequent grammatical errors and limited vocabulary. The use of cohesive devices is minimal, and transitions between ideas are often abrupt or unclear.\n\nFluency: The candidate hesitates frequently, repeats words (\"I really like to wear the jewelry\"), and self-corrects often, which disrupts the flow of speech. There are also instances of incomplete sentences and unclear thoughts, especially in Part 2, which affects the overall fluency.\n\nVocabulary: The range of vocabulary is limited, and there are instances of incorrect word choices (\"beasters\" instead of \"beads\" or \"gemstones\"). The candidate could benefit from using a wider range of topic-specific vocabulary and more precise terms.\n\nGrammar: There are numerous grammatical mistakes, including incorrect verb tenses (\"I should wear the jewelry\"), subject-verb agreement issues (\"this jewelry they can, they can, they can remain about something\"), and incorrect sentence structures. The use of modal verbs is also incorrect at times (\"I wouldn't to enter\").\n\nPronunciation: The transcript does not provide enough information to accurately assess pronunciation.\n\nBand score:5.0 \nFluency: 5.0\nVocabulary: 5.0\nGrammar: 4.5\nPronunciation: 5.0\n\nSpecific topic-words used by candidate (worth-to-mention):\n- Jewelry\n- Chain\n- Bracelet\n- Ring\n- Brilliant\n\nSuggested less used topic-related words, idioms or collocations:\n- Accessorize (as a verb, e.g., \"I like to accessorize with jewelry.\")\n- Gemstones (instead of \"brilliant\")\n- Keepsake (for a piece of jewelry with sentimental value)\n- Timepiece (for a watch)\n- Heirloom (for jewelry passed down through generations)\n- \"Lose track of\" (instead of \"lose this jewelry\")\n- \"Misplace\" (a more accurate verb for losing something)\n- \"Cherished gift\" (instead of \"someone present to me\")\n- \"Hold sentimental value\" (instead of \"they can remain about something\")
 """

one_shot_examples = [
    {"role": "user", "content": content_user},
    {"role": "assistant", "content": content_assis}
]


all_feedback = []
batch_size = 100
output_filename = 'first_feedback_responses.json'

def save_feedback_to_file(feedback_list):
    # Load existing data from the file if it exists
    if os.path.exists(output_filename):
        with open(output_filename, 'r') as output_file:
            existing_data = json.load(output_file)
    else:
        existing_data = []

    # Append new feedback to the existing data
    existing_data.extend(feedback_list)

    # Save the combined data back to the file
    with open(output_filename, 'w') as output_file:
        json.dump(existing_data, output_file, indent=4)
    
    print(f"Batch of {len(feedback_list)} feedback responses added to {output_filename}.")

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        with open(os.path.join(directory, filename), 'r') as file:
            transcript = file.read()

            user_message = {
                "role": "user",
                "content": transcript
            }

            chat_completion = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[
                    system_message_modified,
                    *one_shot_examples,
                    user_message
                ],
                max_tokens=1024,
                temperature=0.7
            )

            model_response = chat_completion.choices[0].message.content

            session_number = ''.join(filter(str.isdigit, filename))

            all_feedback.append({
                "session": session_number,
                "feedback": model_response
            })

            if len(all_feedback) >= batch_size:
                save_feedback_to_file(all_feedback)
                all_feedback = []  # Clear the list after saving

# Save any remaining feedback that didn't make up a full batch
if all_feedback:
    save_feedback_to_file(all_feedback)
