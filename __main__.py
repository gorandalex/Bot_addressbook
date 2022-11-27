from Bot import Bot


def main():
    COMMANDS = {
        'hello': bot.hello,
        'add': bot.add_contact,
        'add phone': bot.add_phone,
        'delete': bot.delete_contact,
        'add email': bot.add_email,
        'add birthday': bot.add_birthday,
        'add_address': bot.add_address,
        'search contact': bot.search_contact,
    #     'add_note': addressbook.add_note,
    #     'add_desc_to_note': addressbook.add_desc_to_note,
    #     'replace_desc_of_note': addressbook.add_desc_to_note,
    #     'search_notes_by_name': addressbook.search_notes_by_name,
    #     'add_tag_to_note': addressbook.add_tag_to_note,
    #     'search_note_by_tags': addressbook.search_notes_by_tags,
    #     'delete_note': addressbook.remove_note,
        'delete_phone': bot.delete_phone,
    #     'delete_email': delete_email,
    #     'delete_address': delete_address,
    #     'sort_func': sorting,
    #     'birthday': birthday,
        'close': bot.answer_exit 
    }
    while True:
        user_command = input('Введіть команду для бота: ').strip().lower()
        command = COMMANDS.get(user_command, Bot.command_error)
        if command == Bot.command_error:
            Bot.command_error(user_command, COMMANDS)
            continue
        else:
            Bot.run_command(command)
        if user_command in ['add', 'remove', 'edit']:
            bot.book.save("auto_save")
        elif user_command == 'close':
            break

if __name__ == "__main__":
    print('Hello. I am your contact-assistant. What should I do with your contacts?')
    bot = Bot()
    bot.book.load("auto_save")
    main()
    
