from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set up your OpenAI API key
openai.api_key = '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'

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_ideas', methods=['POST'])
def generate_ideas():

    category = request.form['category']
    user_prompt = request.form['prompt']
    prompt = f"Generate a sample {category} from the user-input: {user_prompt}"
    print(prompt)
    # Call the OpenAI API to generate ideas
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=2,
        stop=None,
        temperature=0.2
    )
    print(response)
    # Extract the generated ideas from the API response
    ideas = [choice['text'].strip() for choice in response.choices]

    # Render the results template with the generated ideas
    return render_template('results.html', ideas=ideas)


if __name__ == '__main__':
    app.run(debug=True)
