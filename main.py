from microdot import Microdot
from microdot.websocket import with_websocket
import random
import time

app = Microdot()

@app.route('/')
async def index(request):
    html_content = """
        <!DOCTYPE html>
<html>
  <head>
    <title>This is the title of the webpage!</title>
    <script>
      const socket = new WebSocket("ws://192.168.178.107:5000/ws");
      socket.onopen = (event) => {
        // Connection is open
        console.log("opened");
      };
      socket.onmessage = (event) => {
        // Handle incoming messages
        console.log("incoming event: " + event.data);
        document.getElementById("p").innerHTML = event.data;
      };
      socket.onclose = (event) => {
        // Connection is closed
        console.log("closed");
      };
      socket.onerror = (event) => {
        // Handle errors
        console.log("error");
      };
    </script>
  </head>
  <body>
    <p id="p">
      This is an example paragraph. Anything in the <strong>body</strong> tag
      will appear on the page, just like this <strong>p</strong> tag and its
      contents.
    </p>
  </body>
</html>
    """
    return html_content, {'Content-Type': 'text/html'}

@app.route('/ws')
@with_websocket
async def websocket(request, ws):
    while True:
        await ws.send('data')
        time.sleep(5)

app.run()
