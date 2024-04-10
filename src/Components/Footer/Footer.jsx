export default function Footer() {
    const date = new Date();

    return (
        <footer className="absolute bottom-0 text-center bg-neutral-100 w-full py-4 shadow-xs">
            Copyright &copy; {date.getFullYear()}  - All Rights Reserved
        </footer>
    )
}