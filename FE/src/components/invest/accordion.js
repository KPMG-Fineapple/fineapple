import {
  Typography,
  Accordion,
  AccordionSummary,
  AccordionDetails,
} from "@mui/material";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";

export function InvestAccordions(props) {
  const { title, items } = props;
  return (
    <>
      <Typography align="left" variant="subtitle1" sx={{ mb: "20px" }}>
        {title}
      </Typography>
      {items.map((item, idx) => {
        return (
          <Accordion key={idx}>
            <AccordionSummary
              expandIcon={<ExpandMoreIcon />}
              aria-controls="panel1a-content"
              id="panel1a-header"
            >
              <Typography>{item.title}</Typography>
            </AccordionSummary>
            <AccordionDetails>
              <Typography>{item.description}</Typography>
            </AccordionDetails>
          </Accordion>
        );
      })}
    </>
  );
}
