"""
FileProcessor (Template Method)
FileProcessor: Abstract class defining the template method process_file for processing files.
TextFileProcessor: Concrete class extending FileProcessor for processing text files.
CsvFileProcessor: Concrete class extending FileProcessor for processing CSV files.
XmlFileProcessor: Concrete class extending FileProcessor for processing XML files.
Data Processing Framework
FileProcessorFramework: Main framework class that clients will use to process files. It will contain a method process_file which will internally call the template method from FileProcessor.
Sample Files
Include sample text, CSV, and XML files for testing the framework.
Main Application
Main: Main application class that demonstrates how to use the FileProcessorFramework to process different types of files.

"""

from abc import ABC, abstractmethod

# Template Method: FileProcessor
class FileProcessor(ABC):
    @abstractmethod
    def read_file(self, file_path):
        pass

    @abstractmethod
    def parse_data(self, data):
        pass

    @abstractmethod
    def process_data(self, data):
        pass

    def process_file(self, file_path):
        data = self.read_file(file_path)
        parsed_data = self.parse_data(data)
        result = self.process_data(parsed_data)
        return result

# Concrete Classes
class TextFileProcessor(FileProcessor):
    def read_file(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()

    def parse_data(self, data):
        return data.split('\n')

    def process_data(self, data):
        return [line.strip() for line in data if line.strip()]

# CsvFileProcessor and XmlFileProcessor would follow a similar structure.

# Framework
class FileProcessorFramework:
    def __init__(self, processor):
        self.processor = processor

    def process_file(self, file_path):
        return self.processor.process_file(file_path)

# Usage
if __name__ == "__main__":
    text_processor = TextFileProcessor()
    framework = FileProcessorFramework(text_processor)
    result = framework.process_file('sample.txt')
    print(result)
