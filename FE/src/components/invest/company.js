import { Box, Typography, Divider, Button, Avatar } from "@mui/material";
import Image from "next/image";

export function CompanyCard(props) {
  const { companyInfo } = props;
  return (
    <Box sx={{ border: "1px solid #E9ECEF", px: 3 }}>
      <Box
        sx={{
          justifyContent: "space-between",
          display: "flex",
          mt: "15px",
        }}
      >
        <Box
          sx={{
            justifyContent: "space-evenly",
            alignItems: "center",
            display: "flex",
          }}
        >
          <Avatar alt="Remy Sharp" sx={{ mr: 2 }}>
            <Image
              src="/static/images/avatars/avatar_4.png"
              alt="alt"
              layout="fill"
            />
          </Avatar>
          <Typography
            align="center"
            variant="subtitle1"
            sx={{ verticalAlign: "middle" }}
          >
            {companyInfo.name}
          </Typography>
        </Box>
        <Button variant="contained" color="primary" size="small">
          팔로우 하기
        </Button>
      </Box>
      <Divider sx={{ borderColor: "#F2F4F6", my: 2 }} />
      <Typography align="left" variant="subtitle2" sx={{ mb: 2 }}>
        😁 만족도 {companyInfo.satisfaction} 점
      </Typography>
      <Typography align="left" variant="subtitle2" sx={{ mb: 2 }}>
        🔥 누적 투자액 {companyInfo.investAmount.toLocaleString("ko-KR")} 원
      </Typography>
      <Typography align="left" variant="subtitle2" sx={{ mb: 2 }}>
        😎 투자자 {companyInfo.investorNumber.toLocaleString("ko-KR")} 명
      </Typography>
    </Box>
  );
}
