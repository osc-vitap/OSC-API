# OSC-API

<p align="center">
    <a href="https://github.com/Open-Source-Community-VIT-AP/OSC-API"><img src="assets/Long_logo.png" alt="Logo" border="0"></a>
    <br>OSC API that serves JSON data on events.
</p>

## API Endpoints

| ID  | Endpoint                 | Example                                                       | Details                                              |
| --- | ------------------------ | ------------------------------------------------------------- | ---------------------------------------------------- |
| 1   | [/]                      | https://osc-api.herokuapp.com/                                | Index.                                               |
| 1   | [/api/]                  | https://osc-api.herokuapp.com/api/                            | API Base endpoint with documentation                 |
| 2   | [api/event/]             | https://osc-api.herokuapp.com/api/event/                      | GET complete data on all the events.                 |
| 3   | [api/event/\<int:id>]    | https://osc-api.herokuapp.com/api/event/8                     | GET data from a particular event (from Event ID).    |
| 4   | [api/event/latest]       | https://osc-api.herokuapp.com/api/event/latest                | GET data of the latest OSC event.                    |
| 5   | [api/event/announcement] | https://osc-api.herokuapp.com/api/event/announcement?api_key= | POST to this endpoint to send a discord announcement |
| 6   | [api/projects/] | https://osc-api.herokuapp.com/api/projects | GET all public repos from the github organisation. |

## Contributing

To contribute to OSC-API, fork the repository, create a new branch and send us a pull request. Make sure you read [CONTRIBUTING.md](https://github.com/Open-Source-Community-VIT-AP/OSC-API/blob/main/.github/CONTRIBUTING.md) before sending us Pull requests.

Also, thanks for contributing to Open-source!

## License

OSC-API is under The GNU General Public License v3.0. Read the [LICENSE](https://github.com/Open-Source-Community-VIT-AP/OSC-API/blob/main/LICENSE) file for more information.
