import QtQuick 2.5
import QtQuick.Controls 2.5

ApplicationWindow {
    visible: true
    width: 600
    height: 400
    title: '0605-Label'

    Column {
        anchors.centerIn: parent
        spacing: 40

        Label {
            id: mylabel
            text: "Hello World!"
            font.pixelSize: 22     // 字体大小
            font.italic: true      // 斜体
            font.underline: true   // 下划线
            font.bold: true        // 粗体
        }

        Button {
            text: "Click Me"
            height: 40
            width: 100

            onClicked: {
                mylabel.text = "哈哈哈哈哈哈哈哈"
            }
        }
    }
}
