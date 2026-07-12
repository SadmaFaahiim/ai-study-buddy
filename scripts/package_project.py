import os
import zipfile
from pathlib import Path

def package_project():
    """
    Traverses the project folder recursively and compiles it into a ZIP archive,
    filtering out virtual environments, temp caches, logs, and sensitive configurations.
    """
    project_root = Path(__file__).resolve().parent.parent
    zip_filename = project_root / "ai-learning-buddy.zip"
    
    print(f"Project Root: {project_root}")
    print(f"Target ZIP: {zip_filename}")
    
    # Exclude directories
    exclude_dirs = {
        "venv", ".venv", "env", ".git", ".github", "__pycache__", 
        ".pytest_cache", ".streamlit", ".idea", ".vscode"
    }
    
    # Exclude files
    exclude_files = {
        ".env", "ai-learning-buddy.zip", "nohup.out"
    }

    count = 0
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(project_root):
            # Modify dirs in-place to skip excluded directories in recursion
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            for file in files:
                if file in exclude_files or file.endswith((".pyc", ".pyo", ".pyd")):
                    continue
                    
                file_path = Path(root) / file
                relative_path = file_path.relative_to(project_root)
                
                print(f"Adding: {relative_path}")
                zip_file.write(file_path, relative_path)
                count += 1
                
    print(f"\n[INFO] Packaging Completed successfully! Added {count} files to {zip_filename.name}")

if __name__ == "__main__":
    package_project()
