import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sc_django.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Não foi possível importar o Django. Está instalado e no seu ambiente?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
