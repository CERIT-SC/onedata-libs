# Onedata Libraries
This is the repository used for storing all the three Onedata REST API, swagger-generated libraries.

## Generation
> To use this generation utility, you need to have Java installed. To install Java on your machine use `apt install java`.

For the libraries generation, you need to run `runner.sh` file:
```bash
# sometimes it is needed to change the file mode
chmod u+x ./runner.sh 
./runner.sh
```
After that, you will have three folders created - Python libraries for one of **Onezone**, **Onepeorvider** and **Onepanel** respectively.

## Library documentation
Each library has its own documentation with usage and examples. This documentation can be found in library's folder with name `README.md`. This is a very general description of the library functions. For detailed specification, use links provided in `README.md` file of each library.

## Libraries usage
After a library generation, we need to import the library to our Python project. It is recommended to have venv (Virtual Environment) created.

```bash 
# creates new virtual environment called venv 
python -m venv venv

# activates virtual env
source venv/bin/activate

# installs the libraries
pip install -e path/to/library/onezone_client/
pip install -e path/to/library/oneprovider_client/
pip install -e path/to/library/onepanel_client/
```
You can then import the libraries using:
```python
import onezone_client
import oneprovider_client
import onepanel_client
```
More information about usage can be found section "Library documentation"