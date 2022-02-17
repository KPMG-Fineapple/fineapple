import { Box, Typography } from "@mui/material";

export function InvestInfoBar(props) {
  const { title, value } = props;
  return (
    <Box
      sx={{
        justifyContent: "space-between",
        display: "flex",
        mt: "15px",
        borderRadius: "30px",
        backgroundColor: "#E6E8F0",
        p: "15px",
      }}
    >
      <Typography align="center" variant="subtitle2">
        {title}
      </Typography>
      <Typography align="center" variant="subtitle1">
        {value}
      </Typography>
    </Box>
  );
}
