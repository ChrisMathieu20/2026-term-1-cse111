def main():
    try:
        with open("products.vcs", "rt") as products_file:
            for row in products_file:
                print(row)
    except ZeroDivisionError as zer_div_err:
        print(zer_div_err)
    except ValueError as val_err:
        print(val_err)
    except (TypeError, IndexError) as error:
        print(error)
    except KeyError as key_err:
        print(type(key_err).__name__, key_err)
    except FileNotFoundError as not_found_err:
        print(not_found_err)
    except PermissionError as perm_err:
        print(perm_err)

if __name__ == "__main__":
    main()