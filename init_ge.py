from great_expectations.data_context import FileDataContext

def init_ge_project():
    context = FileDataContext.create()
    print(f"GE project initialized at: {context.root_directory}")

if __name__ == "__main__":
    init_ge_project()
