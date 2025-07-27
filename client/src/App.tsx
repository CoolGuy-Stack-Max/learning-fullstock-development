import { useState } from "react";
import { Button, DatePicker, Input, Table, Modal, Form, message } from "antd";
import dayjs from "dayjs";
// import "antd/dist/antd.css";
import "@ant-design/v5-patch-for-react-19";

const App = () => {
  const [data, setData] = useState([
    {
      key: "1",
      orderNo: "A001",
      customerName: "张三",
      orderDate: "2025-07-23",
    },
    {
      key: "2",
      orderNo: "A002",
      customerName: "李四",
      orderDate: "2025-07-24",
    },
  ]);
  const [isModalVisible, setIsModalVisible] = useState(false);
  const [editingOrder, setEditingOrder] = useState<any>(null);

  // 显示弹窗
  const showModal = () => {
    setIsModalVisible(true);
    setEditingOrder(null); // 重置编辑状态
  };

  // 关闭弹窗
  const handleCancel = () => {
    setIsModalVisible(false);
  };

  // 提交表单
  const handleOk = (values: any) => {
    // debugger;
    if (editingOrder) {
      // 编辑订单
      setData((prevData) =>
        prevData.map((item) =>
          item.key === editingOrder.key
            ? {
                ...item,
                ...values,
                orderDate: values.orderDate.format("YYYY-MM-DD"),
              }
            : item
        )
      );
      message.success("订单已更新");
    } else {
      // 添加新订单
      setData((prevData) => [
        ...prevData,
        {
          key: Date.now().toString(),
          ...values,
          orderDate: values.orderDate.format("YYYY-MM-DD"),
        },
      ]);
      message.success("新订单已添加");
    }
    setIsModalVisible(false);
  };

  // 编辑订单
  const handleEdit = (record) => {
    setEditingOrder(record);
    setIsModalVisible(true);
  };

  // 删除订单
  const handleDelete = (key) => {
    Modal.confirm({
      title: "确定删除该订单吗?",
      onOk: () => {
        setData((prevData) => prevData.filter((item) => item.key !== key));
        message.success("订单已删除");
      },
    });
  };

  const columns = [
    { title: "订单号", dataIndex: "orderNo", key: "orderNo" },
    { title: "顾客姓名", dataIndex: "customerName", key: "customerName" },
    { title: "订单日期", dataIndex: "orderDate", key: "orderDate" },
    {
      title: "操作",
      key: "action",
      render: (text, record) => (
        <>
          <Button onClick={() => handleEdit(record)} type="link">
            编辑
          </Button>
          <Button onClick={() => handleDelete(record.key)} type="link" danger>
            删除
          </Button>
        </>
      ),
    },
  ];

  return (
    <div style={{ padding: 20 }}>
      <h1 style={{ color: "black" }}>消费者订单记录</h1>
      <Button type="primary" onClick={showModal} style={{ marginBottom: 16 }}>
        新增订单
      </Button>
      <Table columns={columns} dataSource={data} />

      {/* 弹窗用于新增或编辑订单 */}
      <Modal
        title={editingOrder ? "编辑订单" : "新增订单"}
        open={isModalVisible}
        onCancel={handleCancel}
        footer={null}
      >
        <Form
          initialValues={{
            ...editingOrder,
            orderDate: editingOrder ? dayjs(editingOrder.orderDate) : null, // 确保日期格式正确
          }}
          onFinish={handleOk}
          layout="vertical"
        >
          <Form.Item
            label="订单号"
            name="orderNo"
            rules={[{ required: true, message: "请输入订单号" }]}
          >
            <Input />
          </Form.Item>
          <Form.Item
            label="顾客姓名"
            name="customerName"
            rules={[{ required: true, message: "请输入顾客姓名" }]}
          >
            <Input />
          </Form.Item>
          <Form.Item
            label="订单日期"
            name="orderDate"
            rules={[{ required: true, message: "请选择订单日期" }]}
          >
            <DatePicker style={{ width: "100%" }} format="YYYY-MM-DD" />
          </Form.Item>
          <Form.Item>
            <Button type="primary" htmlType="submit">
              {editingOrder ? "更新订单" : "新增订单"}
            </Button>
          </Form.Item>
        </Form>
      </Modal>
    </div>
  );
};

export default App;
