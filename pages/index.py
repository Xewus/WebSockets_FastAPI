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
        <div>
          <div class="col-sm-8 py-5 mx-auto">
            <div class="card">
              <h1 class="card-header" style="display: flex; justify-content: center">
                Сообщения
              </h1>
              <div class="card-body" style="display: flex; justify-content: center">
                <form onsubmit="sendMessage(event)">
                  <input required type="text" id="messageText" autocomplete="off"/>
                  <button>Отправить</button>
                </form>
              </div>
              <div id="messages" class="card-body">
              </div><!-- card-body -->
            </div><!-- card -->
          </div><!-- col -->
        </div><!-- rounded -->
      </main>
    </div><!-- bg-image -->

    <script>
        var ws = new WebSocket("%8s");
        ws.onmessage = function(event) {
            var data = JSON.parse(event.data)
            if (data.status == 400) {
                alert(data.text)
            } else if (data.status == 200) {
                var messages = document.getElementById("messages")
                var message = document.createElement('ol')
                var content = document.createTextNode(data.num + ": " + data.text);
                message.appendChild(content)
                messages.appendChild(message)
            } else {
              alert("Неизвестная ошибка")
            }
        };

        function sendMessage(event) {
            if (ws.readyState === ws.OPEN) {
                var input = document.getElementById("messageText")
                var data = {
                    "text": document.getElementById("messageText").value
                };
                ws.send(JSON.stringify(data));
                input.value = ""
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
