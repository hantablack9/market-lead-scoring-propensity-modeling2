import os
from dataclasses import dataclass

import rarfile


@dataclass
class RarExtractor:
    RarExtractor
    A utility class for extracting .csv files from .rar archives to a specified directory.
    Attributes:
        rar_path (str): Path to the .rar archive file.
        extract_to (str): Directory where the extract file will be saved. Defaults to "./data".
        output_filename (str): Desired name for the extracted CSV file. Defaults to "dataset.csv". # type: ignore
        auto_rename (bool): If True, automatically renames the output file to avoid overwriting existing files.
    Methods:
        _resolve_versioned_filename():
            Determines a unique filename by appending a version number if a file with the desired name already exists.
        extract():
            Extracts the first .csv file found in the .rar archive to the target directory.
            If auto_rename is enabled, ensures the output filename does not overwrite existing files.
            Returns the path to the extracted CSV file.
            Raises FileNotFoundError if no .csv file is found in the archive.
            Raises FileExistsError if auto_rename is False and the output file already exists.
    """
    Handles extraction of .rar files to a specified directory.
    """

    rar_path: str
    extract_to: str = "./data"
    output_filename: str = "dataset.csv"
    auto_rename: bool = True

    def _resolve_versioned_filename(self) -> str:
        """
        Resolve a versioned filename if auto_rename is enabled.
        This ensures that if the output file already exists, a new versioned
        filename is created.
        """
        base, ext = os.path.splitext(self.output_filename)
        candidate = os.path.join(self.extract_to, self.output_filename)
        count = 1
        while os.path.exists(candidate):
            candidate = os.path.join(self.extract_to, f"{base}_{count}{ext}")
            count += 1
        return candidate

    def extract(self) -> str:
        """
        Extracts the .csv file from the .rar archive and returns the path to the extracted CSV file.
        """
        if not os.path.exists(self.extract_to):
            os.makedirs(self.extract_to)

        with rarfile.RarFile(self.rar_path) as rf:
            for name in rf.namelist():
                if name.endswith(".csv"):
                    destination = (
                        self._resolve_versioned_filename()
                        if self.auto_rename
                        else os.path.join(self.extract_to, self.output_filename)
                    )
                    if not self.auto_rename and os.path.exists(destination):
                        raise FileExistsError(f"[ERROR] {destination} already exists.")

                    print(f"[INFO] Extracting {name} to {destination}")
                    rf.extract(name, path=self.extract_to)
                    os.rename(os.path.join(self.extract_to, name), destination)
                    return destination

        raise FileNotFoundError("❌ No .csv file found in RAR archive.")
