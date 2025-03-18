import QtQuick 2.5
import QtQuick.Controls 2.5

ApplicationWindow {
    visible: true
    width: 600
    height: 400
    title: '0604 Row and Column'

    Row {
        spacing: 10  // 间距

        anchors.centerIn: parent

        Column {
            spacing: 10

            Rectangle {
                color: 'red'; width: 50; height: 50
            }
            Rectangle {
                color: 'green'; width: 50; height: 50
            }
            Rectangle {
                color: 'blue'; width: 50; height: 50
            }
        }

        Column {
            spacing: 10
            Rectangle {
                color: 'green'; width: 50; height: 50
            }
            Rectangle {
                color: 'blue'; width: 50; height: 50
            }
            Rectangle {
                color: 'red'; width: 50; height: 50
            }
        }

        Column {
            spacing: 10
            Rectangle {
                color: 'blue'; width: 50; height: 50
            }
            Rectangle {
                color: 'red'; width: 50; height: 50
            }
            Rectangle {
                color: 'green'; width: 50; height: 50
            }
        }
    }
}
