// Code generated by protoc-gen-go. DO NOT EDIT.
// source: mortar.proto

package proto

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	math "math"
)

import (
	context "golang.org/x/net/context"
	grpc "google.golang.org/grpc"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion2 // please upgrade the proto package

type QualifyRequest struct {
	// all of these queries must return a response for the site to be considered
	// qualified
	Requiredqueries []*QueryRequest `protobuf:"bytes,1,rep,name=requiredqueries,proto3" json:"requiredqueries,omitempty"`
	// only one of these needs to return a response for the site to be
	// considered qualified
	Optionalqueries      []*QueryRequest `protobuf:"bytes,2,rep,name=optionalqueries,proto3" json:"optionalqueries,omitempty"`
	XXX_NoUnkeyedLiteral struct{}        `json:"-"`
	XXX_unrecognized     []byte          `json:"-"`
	XXX_sizecache        int32           `json:"-"`
}

func (m *QualifyRequest) Reset()         { *m = QualifyRequest{} }
func (m *QualifyRequest) String() string { return proto.CompactTextString(m) }
func (*QualifyRequest) ProtoMessage()    {}
func (*QualifyRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_1d43959f7c3049fd, []int{0}
}
func (m *QualifyRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_QualifyRequest.Unmarshal(m, b)
}
func (m *QualifyRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_QualifyRequest.Marshal(b, m, deterministic)
}
func (m *QualifyRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_QualifyRequest.Merge(m, src)
}
func (m *QualifyRequest) XXX_Size() int {
	return xxx_messageInfo_QualifyRequest.Size(m)
}
func (m *QualifyRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_QualifyRequest.DiscardUnknown(m)
}

var xxx_messageInfo_QualifyRequest proto.InternalMessageInfo

func (m *QualifyRequest) GetRequiredqueries() []*QueryRequest {
	if m != nil {
		return m.Requiredqueries
	}
	return nil
}

func (m *QualifyRequest) GetOptionalqueries() []*QueryRequest {
	if m != nil {
		return m.Optionalqueries
	}
	return nil
}

type QualifyResponse struct {
	Error string `protobuf:"bytes,1,opt,name=error,proto3" json:"error,omitempty"`
	// list of sitenames
	Sites                []string `protobuf:"bytes,2,rep,name=sites,proto3" json:"sites,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *QualifyResponse) Reset()         { *m = QualifyResponse{} }
func (m *QualifyResponse) String() string { return proto.CompactTextString(m) }
func (*QualifyResponse) ProtoMessage()    {}
func (*QualifyResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_1d43959f7c3049fd, []int{1}
}
func (m *QualifyResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_QualifyResponse.Unmarshal(m, b)
}
func (m *QualifyResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_QualifyResponse.Marshal(b, m, deterministic)
}
func (m *QualifyResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_QualifyResponse.Merge(m, src)
}
func (m *QualifyResponse) XXX_Size() int {
	return xxx_messageInfo_QualifyResponse.Size(m)
}
func (m *QualifyResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_QualifyResponse.DiscardUnknown(m)
}

var xxx_messageInfo_QualifyResponse proto.InternalMessageInfo

func (m *QualifyResponse) GetError() string {
	if m != nil {
		return m.Error
	}
	return ""
}

func (m *QualifyResponse) GetSites() []string {
	if m != nil {
		return m.Sites
	}
	return nil
}

func init() {
	proto.RegisterType((*QualifyRequest)(nil), "proto.QualifyRequest")
	proto.RegisterType((*QualifyResponse)(nil), "proto.QualifyResponse")
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConn

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion4

// MortarClient is the client API for Mortar service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type MortarClient interface {
	// returns list of sites that match the qualification filter
	Qualify(ctx context.Context, in *QualifyRequest, opts ...grpc.CallOption) (*QualifyResponse, error)
}

type mortarClient struct {
	cc *grpc.ClientConn
}

func NewMortarClient(cc *grpc.ClientConn) MortarClient {
	return &mortarClient{cc}
}

func (c *mortarClient) Qualify(ctx context.Context, in *QualifyRequest, opts ...grpc.CallOption) (*QualifyResponse, error) {
	out := new(QualifyResponse)
	err := c.cc.Invoke(ctx, "/proto.Mortar/Qualify", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// MortarServer is the server API for Mortar service.
type MortarServer interface {
	// returns list of sites that match the qualification filter
	Qualify(context.Context, *QualifyRequest) (*QualifyResponse, error)
}

func RegisterMortarServer(s *grpc.Server, srv MortarServer) {
	s.RegisterService(&_Mortar_serviceDesc, srv)
}

func _Mortar_Qualify_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(QualifyRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(MortarServer).Qualify(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/proto.Mortar/Qualify",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(MortarServer).Qualify(ctx, req.(*QualifyRequest))
	}
	return interceptor(ctx, in, info, handler)
}

var _Mortar_serviceDesc = grpc.ServiceDesc{
	ServiceName: "proto.Mortar",
	HandlerType: (*MortarServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Qualify",
			Handler:    _Mortar_Qualify_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "mortar.proto",
}

func init() { proto.RegisterFile("mortar.proto", fileDescriptor_1d43959f7c3049fd) }

var fileDescriptor_1d43959f7c3049fd = []byte{
	// 244 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xe2, 0xe2, 0xc9, 0xcd, 0x2f, 0x2a,
	0x49, 0x2c, 0xd2, 0x2b, 0x28, 0xca, 0x2f, 0xc9, 0x17, 0x62, 0x05, 0x53, 0x52, 0x9c, 0x19, 0xf9,
	0x29, 0x10, 0x11, 0x29, 0x99, 0xf4, 0xfc, 0xfc, 0xf4, 0x9c, 0x54, 0xfd, 0xc4, 0x82, 0x4c, 0xfd,
	0xc4, 0xbc, 0xbc, 0xfc, 0x92, 0xc4, 0x92, 0xcc, 0xfc, 0xbc, 0x62, 0x88, 0xac, 0x52, 0x1f, 0x23,
	0x17, 0x5f, 0x60, 0x69, 0x62, 0x4e, 0x66, 0x5a, 0x65, 0x50, 0x6a, 0x61, 0x69, 0x6a, 0x71, 0x89,
	0x90, 0x2d, 0x17, 0x7f, 0x51, 0x6a, 0x61, 0x69, 0x66, 0x51, 0x6a, 0x4a, 0x61, 0x69, 0x6a, 0x51,
	0x66, 0x6a, 0xb1, 0x04, 0xa3, 0x02, 0xb3, 0x06, 0xb7, 0x91, 0x30, 0x44, 0x8f, 0x5e, 0x60, 0x69,
	0x6a, 0x11, 0x4c, 0x75, 0x10, 0xba, 0x5a, 0x90, 0xf6, 0xfc, 0x02, 0x90, 0x15, 0x89, 0x39, 0x30,
	0xed, 0x4c, 0x78, 0xb4, 0xa3, 0xa9, 0x55, 0xb2, 0xe5, 0xe2, 0x87, 0xbb, 0xa7, 0xb8, 0x20, 0x3f,
	0xaf, 0x38, 0x55, 0x48, 0x84, 0x8b, 0x35, 0xb5, 0xa8, 0x28, 0xbf, 0x48, 0x82, 0x51, 0x81, 0x51,
	0x83, 0x33, 0x08, 0xc2, 0x01, 0x89, 0x16, 0x67, 0x96, 0x40, 0x4d, 0xe7, 0x0c, 0x82, 0x70, 0x8c,
	0x12, 0xb9, 0xd8, 0x7c, 0xc1, 0xe1, 0x21, 0x14, 0xce, 0xc5, 0x0e, 0x35, 0x48, 0x48, 0x14, 0x6e,
	0x33, 0xb2, 0x47, 0xa5, 0xc4, 0xd0, 0x85, 0x21, 0xf6, 0x29, 0xc9, 0x36, 0x5d, 0x7e, 0x32, 0x99,
	0x49, 0x5c, 0x49, 0x48, 0xbf, 0xcc, 0x50, 0x1f, 0x12, 0xba, 0xfa, 0x85, 0x10, 0x35, 0x56, 0x8c,
	0x5a, 0x49, 0x6c, 0x60, 0x5d, 0xc6, 0x80, 0x00, 0x00, 0x00, 0xff, 0xff, 0x06, 0x0c, 0x92, 0x7e,
	0x79, 0x01, 0x00, 0x00,
}
