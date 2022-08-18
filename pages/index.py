index = '''
<!DOCTYPE html>
<html lang="ru">
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Messenger</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
  </head>

   <body>
    <div
      class="bg-image"
      style="
        background-image: url('https://mdbcdn.b-cdn.net/img/Photos/Others/images/77.webp');
        height: 100vh;
      "
    >
      <main>
        <div class="container row justify-content-center">
          <div class="col-md-8 p-5">
            <div class="card">
              <div class="card-header" style="display: flex; justify-content: center">
                <h1>Сообщения</h1>
              </div>
              <div class="card-body" style="display: flex; justify-content: center">
                <form onsubmit="sendMessage(event)">
                  <input required type="text" id="messageText" autocomplete="off"/>
                  <button>Отправить</button>
                </form>
              </div>
              <div id="messages" class="card-body">
              </div>
            </div><!-- card -->
          </div><!-- col -->
        </div><!-- container-->
      </main>
    </div><!-- bg-image -->

    <script>
        var ws = new WebSocket("%s");

        ws.onmessage = function(event) {
            var data = JSON.parse(event.data)

            if (data.status == 400) {
                alert(data.error)
            } else if (data.status == 201) {
                var messages = document.getElementById('messages')
                var message = document.createElement('ol')
                var content = document.createTextNode(data.number + ": " + data.message);
                message.appendChild(content)
                messages.appendChild(message)
            }
        };

        function sendMessage(event) {
            if (ws.readyState === ws.OPEN) {
                var input = document.getElementById("messageText")
                var data = {
                    "message": document.getElementById("messageText").value
                };
                ws.send(JSON.stringify(data));
                input.value = ''
                event.preventDefault()
            } else {
                alert("Нет соединения с сервером")
            }
        }
    </script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
  </body>
</html>
'''
