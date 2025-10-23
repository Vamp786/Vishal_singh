from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'angry_bird'  # Needed for flash messages

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    gmail = request.form.get('gmail')
    message = request.form.get('message')

    if not name or not gmail or not message:
        flash('Please fill all the fields.', 'error')
        return redirect(url_for('home'))

    # Here you can add logic to save the message or send email
    print(f"New message from {name} ({gmail}): {message}")

    flash(f'Thank you, {name}! Your message has been received.', 'success')
    return redirect(url_for('home'))

# Debugging route for static files
@app.route('/static/<path:filename>')
def static_files(filename):
    from flask import send_from_directory
    import os
    static_folder = os.path.join(app.root_path, 'static')
    return send_from_directory(static_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)