
    while True:

      print("\n========== PHONEBOOK ==========")

      print("1. Add Contact")
      print("2. Import CSV")
      print("3. Show Contacts")
      print("4. Search Contact")
      print("5. Search Email")
      print("6. Update Contact")
      print("7. Delete Contact")
      print("8. Filter By Group")
      print("9. Sort Contacts")
      print("10. Add Phone")
      print("11. Move Contact To Group")
      print("12. Pagination")
      print("13. Export JSON")
      print("14. Import JSON")
      print("15. Exit")

      choice = input("Select Option: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        import_csv()

    elif choice == "3":
        show_contacts()

    elif choice == "4":
        search_contact()

    elif choice == "5":
        search_email()

    elif choice == "6":
        update_contact()

    elif choice == "7":
        delete_contact()

    elif choice == "8":
        filter_group()

    elif choice == "9":
        sort_contacts()

    elif choice == "10":
        add_phone()

    elif choice == "11":
        move_group()

    elif choice == "12":
        pagination()

    elif choice == "13":
        export_json()

    elif choice == "14":
        import_json()

    elif choice == "15":

        print("Thank You!")

        break

    else:

        print("Invalid Choice!")