export default function Header({ title }) {
    return (
        <h1 className="font-semibold text-2xl">{title}</h1>
    )
}
Header.defaultProps = {
    title: 'TradeVista',
}