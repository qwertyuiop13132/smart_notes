from PyQt6.QtWidgets import QMainWindow,QApplication, QInputDialog
import json
from ui import Ui_MainWindow

app = QApplication([])
win = QMainWindow()
ui = Ui_MainWindow()

ui.setupUi(win)


NOTES = {
}


with open("notes_data.json", "r", encoding="utf-8") as file:
    NOTES = json.load(file)

ui.notest_list.addItems(NOTES)

def show_note():
    print("note selected")
    if ui.notest_list.currentItem():
        none_name = ui.notest_list.currentItem().text()
        note = NOTES[none_name]
        ui.textEdit.setText(note["текст"])
        ui.tag_list.clear()
        ui.tag_list.addItems(note["теги"])

ui.notest_list.currentItemChanged.connect(show_note)

def add_note():
    note_name, OK = QInputDialog.getText(win, "+ нотатки", "назва")
    if OK:
        NOTES[note_name] = {
            "текст": "",
            "теги": []
        }
        ui.notest_list.addItem(note_name)
ui.add_note.clicked.connect(add_note)

def save_note():
    if ui.notest_list.currentItem():
        note_name = ui.notest_list.currentItem().text()
        text = ui.textEdit.toPlainText()
        NOTES[note_name]["текст"] = text


        with open("notes_data.json", "w", encoding="utf_8") as file:
            json.dump(NOTES, file)
ui.save_note.clicked.connect(save_note)

def del_note():
    if ui.notest_list.currentItem():
        note_name = ui.notest_list.currentItem().text()
        del NOTES[note_name]
        with open("notes_data.json", "w", encoding="utf_8") as file:
            json.dump(NOTES, file)
        ui.notest_list.clear()
        ui.notest_list.addItem(NOTES)

        ui.textEdit.clear()
        ui.tag_list.clear()
ui.del_note.clicked.connect(del_note)

def add_teg():
    if ui.notest_list.currentItem():
        note_name = ui.notest_list.currentItem().text()
        note = NOTES[note_name]

        new_teg = ui.tag_input.text()

        if new_teg not in note["теги"]:
            note["теги"].append(new_teg)
            ui.tag_list.addItem(new_teg)

ui.add_tag.clicked.connect(add_teg)

def del_teg():
    if ui.tag_list.currentItem():
        tag = ui.tag_list.currentItem().text()
        note_name = ui.notest_list.currentItem().text()
        note = NOTES[note_name]
        if tag  in note["теги"]:
            note["теги"].remove(tag)
            ui.tag_list.clear()
            ui.tag_list.addItems(note["теги"])
ui.del_tag.clicked.connect(del_teg)

def search_teg():
    if ui.search_btb.text() == "шук нот по тегу":
        tag = ui.tag_input.text()
        filtered_notes = []
        for note_name, note in NOTES.items():
            if tag in note["теги"]:
                filtered_notes.append(note_name)
        ui.notest_list.clear()
        ui.notest_list.addItems(filtered_notes)
        
        ui.search_btb.setText("скинути пошук")
    elif ui.search_btb.text() == "скинути пошук":
        ui.tag_input.clear()
        ui.notest_list.clear()
        ui.notest_list.addItems(NOTES)
        

        ui.search_btb.setText("шук нот по тегу")

ui.search_btb.clicked.connect(search_teg)
print("102910445463374")
win.show()
app.exec()