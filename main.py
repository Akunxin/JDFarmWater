from flask import Flask, render_template, request
from markupsafe import Markup
import markdown
import markdown.extensions.fenced_code
import markdown.extensions.codehilite

import water

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('index.html')


@app.route('/get_response', methods=['POST'])
def response():
  user_input = request.form['user_input']
  messages = water.water(user_input)
  # 将字符串转换为 HTML 格式并标记为安全的
  response_html = Markup(
    markdown.markdown(messages, extensions=['fenced_code', 'codehilite']))
  return response_html


if __name__ == '__main__':
  app.run(host='0.0.0.0', threaded=True, debug=False, port=5001)
