import { Button, Checkbox, Col, Input, Row} from "antd";

ReactDOM.render(
  <Row gutter={10} align="middle">
    <Col>
      <Checkbox>I agree.</Checkbox>
    </Col>
    <Col>
      <Button>Click me!</Button>
    </Col>
    <Col>
      <Input placeholder="Your name"/>
    </Col>
  </Row>,
  mountNode
);
