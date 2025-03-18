import QtQuick 2.5
import QtQuick.Controls 2.5

ApplicationWindow {
    visible: true
    width: 600
    height: 400
    title: '0603-Button'

    Button {
        text: '点击我'
        id: button
        // x: 70
        // y: 70
        // height: 40
        // width: 100
        anchors.centerIn: parent  // 居中在父级视图
        background: Rectangle {
            implicitWidth: 100
            implicitHeight: 40
            color: button.down ? "#d6d6d6" : "#f6f6f6"
            border.color: "#2628aa"
            border.width: 1
            radius: 4
        }

        onClicked: {
            window.hello()
        }
    }
}
