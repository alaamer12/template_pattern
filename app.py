"""

Sure, let's create a comprehensive project utilizing the Template Method design pattern.

Project Overview:
We'll create a simple application to manage various types of documents. These documents could include reports, presentations, and spreadsheets. Each document type will have its own steps for creation, such as opening, editing, and saving. We'll use the Template Method design pattern to define a skeleton of the document creation process, allowing subclasses to override certain steps while keeping others fixed.

Project Structure:

Document (Abstract Class): Defines the template method createDocument() that outlines the steps for creating a document.
Report (Concrete Class): Implements the steps specific to creating a report document.
Presentation (Concrete Class): Implements the steps specific to creating a presentation document.
Spreadsheet (Concrete Class): Implements the steps specific to creating a spreadsheet document.
Main (Class): Contains the main method to demonstrate the functionality of the application.
"""

from abc import ABC, abstractmethod


# Document class with template method
class Document(ABC):

    def create_document(self):
        self.open_document()
        self.edit_document()
        self.save_document()
        self.close_document()

    @abstractmethod
    def open_document(self):
        pass

    @abstractmethod
    def edit_document(self):
        pass

    @abstractmethod
    def save_document(self):
        pass

    @abstractmethod
    def close_document(self):
        pass


# Concrete classes for different types of documents
class Report(Document):

    def open_document(self):
        print("Opening Report...")

    def edit_document(self):
        print("Editing Report...")

    def save_document(self):
        print("Saving Report...")

    def close_document(self):
        print("Closing Report...")


class Presentation(Document):

    def open_document(self):
        print("Opening Presentation...")

    def edit_document(self):
        print("Editing Presentation...")

    def save_document(self):
        print("Saving Presentation...")

    def close_document(self):
        print("Closing Presentation...")


class Spreadsheet(Document):

    def open_document(self):
        print("Opening Spreadsheet...")

    def edit_document(self):
        print("Editing Spreadsheet...")

    def save_document(self):
        print("Saving Spreadsheet...")

    def close_document(self):
        print("Closing Spreadsheet...")


# Main function
def main():
    # Create and process different types of documents
    report = Report()
    presentation = Presentation()
    spreadsheet = Spreadsheet()

    print("Creating Report:")
    report.create_document()
    print()

    print("Creating Presentation:")
    presentation.create_document()
    print()

    print("Creating Spreadsheet:")
    spreadsheet.create_document()


if __name__ == "__main__":
    main()
