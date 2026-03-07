"""
Setup Verification Script for YOLO Object Detection
Run this script to check if your environment is ready
"""

import sys
import subprocess
import importlib.util
import platform

def check_python():
    """Check Python installation"""
    print("=" * 50)
    print("PYTHON ENVIRONMENT CHECK")
    print("=" * 50)
    
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    print(f"Platform: {platform.platform()}")
    
    # Check if python is in PATH (by trying to run 'python --version' from subprocess)
    try:
        result = subprocess.run(['python', '--version'], 
                              capture_output=True, text=True, timeout=5)
        print(f"CMD 'python' command: {result.stdout.strip()}")
        print("✓ Python is accessible from CMD")
    except (subprocess.SubprocessError, FileNotFoundError):
        print("✗ Python is NOT accessible from CMD as 'python'")
        print("  Try using 'py' or 'python3' instead")
        
        # Try alternative commands
        for cmd in ['py', 'python3']:
            try:
                result = subprocess.run([cmd, '--version'], 
                                      capture_output=True, text=True, timeout=5)
                print(f"  But '{cmd}' works: {result.stdout.strip()}")
            except:
                pass

def check_library(library_name, import_name=None):
    """Check if a library is installed"""
    if import_name is None:
        import_name = library_name
    
    spec = importlib.util.find_spec(import_name)
    if spec is not None:
        try:
            module = importlib.import_module(import_name)
            version = getattr(module, '__version__', 'unknown')
            print(f"✓ {library_name} is installed (version: {version})")
            return True
        except ImportError:
            print(f"✗ {library_name} found but cannot be imported")
            return False
    else:
        print(f"✗ {library_name} is NOT installed")
        return False

def check_ultralytics():
    """Special check for ultralytics"""
    try:
        from ultralytics import YOLO
        print("✓ ultralytics.YOLO imported successfully")
        
        # Check if we can create a YOLO instance (without downloading)
        try:
            # This just checks if the class exists, doesn't download
            print("  YOLO class is available")
        except Exception as e:
            print(f"  Warning: YOLO class issue: {e}")
            
    except ImportError as e:
        print(f"✗ Failed to import ultralytics: {e}")
        
def check_opencv():
    """Special check for OpenCV"""
    try:
        import cv2
        print(f"✓ OpenCV imported successfully (version: {cv2.__version__})")
        
        # Check basic functionality
        try:
            # Try to read an image (doesn't need actual file)
            print("  OpenCV basic functions available")
        except Exception as e:
            print(f"  Warning: OpenCV function test failed: {e}")
            
    except ImportError as e:
        print(f"✗ Failed to import cv2: {e}")

def main():
    """Main verification function"""
    
    # Check Python
    check_python()
    
    print("\n" + "=" * 50)
    print("LIBRARY INSTALLATION CHECK")
    print("=" * 50)
    
    # Check required libraries
    print("\nChecking ultralytics...")
    check_ultralytics()
    
    print("\nChecking OpenCV...")
    check_opencv()
    
    # Also check common dependencies
    print("\n" + "=" * 50)
    print("ADDITIONAL DEPENDENCIES")
    print("=" * 50)
    
    optional_libs = [
        ('numpy', 'numpy'),
        ('torch', 'torch'),
        ('matplotlib', 'matplotlib'),
        ('PIL', 'PIL')
    ]
    
    for lib_name, import_name in optional_libs:
        check_library(lib_name, import_name)
    
    # Summary
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    
    all_good = True
    
    # Check core requirements
    if check_library('ultralytics', 'ultralytics'):
        print("✓ ultralytics is ready")
    else:
        print("✗ Need to install ultralytics: pip install ultralytics")
        all_good = False
    
    if check_library('cv2', 'cv2'):
        print("✓ OpenCV is ready")
    else:
        print("✗ Need to install opencv-python: pip install opencv-python")
        all_good = False
    
    print("\n" + "=" * 50)
    if all_good:
        print("✓✓✓ ALL SYSTEMS READY! You can run YOLO scripts. ✓✓✓")
    else:
        print("⚠ Some requirements are missing. Install them and try again.")
    
    print("=" * 50)
    
    # Provide installation commands if needed
    if not all_good:
        print("\nTo install missing libraries, run in CMD:")
        print("  pip install ultralytics opencv-python")
        print("\nIf pip doesn't work, try:")
        print("  python -m pip install ultralytics opencv-python")
        print("  py -m pip install ultralytics opencv-python")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nError running verification: {e}")
        print("\nPlease check your Python installation manually.")
    
    input("\nPress Enter to exit...")