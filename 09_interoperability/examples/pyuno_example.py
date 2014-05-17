import socket
import uno

# soffice "-accept=socket,host=localhost,port=2002;urp;"

# Получаем контекст UNO
localContext = uno.getComponentContext()

resolver = localContext.ServiceManager.createInstanceWithContext(
				"com.sun.star.bridge.UnoUrlResolver", localContext)
# Соединяемся с OpenOffice
ctx = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
smgr = ctx.ServiceManager
# Получаем главное окно
desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
# Получаем текущий открытый документ
model = desktop.getCurrentComponent()
# Получаем текст текущего документа
text = model.Text
# Создаём курсор
cursor = text.createTextCursor()
# Вставляем по курсору текст
text.insertString(cursor, "Hello World", 0)
