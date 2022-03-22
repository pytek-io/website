### A Python enterprise framework

Reflect is a complete solution that allows the simple development of business apps (aka [Single Page Application](https://en.wikipedia.org/wiki/Single-page_application)), all in Python. It exposes many [React](https://reactjs.org/) component libraries to Python and provides a powerful high level API to drive these components. Apps are Python scripts which can be launched from a web browser.

## General architecture

Central to the Reflect architecture, is a high performance application server written in [Rust](https://www.rust-lang.org/) which connects client web apps to Python processes called kernels. Kernels can drive one or many apps at once, depending on the specified kernel policy. A Reflect application server can easily be connected to a source control management solution, making app deployment as easy as a code push.

The figure below features a highly simplified setup in which a few apps are run by a couple of kernels. The client machines can either access the server through the internet, a private network, or be run on the same machine. Reflect server is a high performance application which can run on pretty much any hardware from lightweight virtual servers to beefy physical machines. Client machines can be any device running a recent enough internet browser. A server can run between dozens and thousands of apps depending on many factors, such as the server capacity, the apps requirements, the kernel policy, etc. Either way, the underlying architecture is very flexible and can be easily scaled through traditional web load balancers.
![Reflect architecture](/website/reflect_architecture.svg)

### Summary

- Reflect provides an application server turning Python scripts into web apps.
- Kernels are python processes managed by the application server on which apps run.
- Apps can easily be deployed, thanks to an easy integration with source control management.
